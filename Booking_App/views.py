from django.db.models import Subquery
from django.shortcuts import render, redirect
from .models import *
from Admin.models import TimeSlotTable
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
"Loading the Booking Page "


def booking(request):
    userid = request.session['userid']
    user_details = User.objects.get(id=userid)
    return render(request, 'bookingPage.html', {'userDetails': user_details})


"Booking the time slot and putting into database"


def bookTimeSlot(request):
    book = False
    if request.method == 'POST':
        userid = request.session['userid']
        user_id = User.objects.get(id=userid)
        phone = request.POST["visitor_phone"]
        no_of_hours = request.POST["total_hours"]
        booking_date = request.POST["book_date"]
        timeslot = request.POST["hour_preference"]
        note = request.POST["message"]
        amount = request.POST["total_amount"]

        if BookingTable.objects.filter(booking_date=booking_date, time_slot=timeslot).exists():
            messages.info(request, 'Already Booked')
            return redirect('booking')
        else:
            booking = BookingTable.objects.create(userid=user_id, phone=phone, hours_need=no_of_hours,
                                                  booking_date=booking_date, time_slot=timeslot,
                                                  amount=amount, note=note, book_status='pending')
            booking.save()
            book = True
    return render(request, 'bookingPage.html', {'booked': book})
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


"AJAX FUNCTION TO GET AVAILABLE TIME SLOT "


def load_available_timeSlot(request):
    date_value = request.GET.get('date_value')
    booked_timeSlot = BookingTable.objects.filter(booking_date=date_value, book_status='pending')
    time_slots = TimeSlotTable.objects.exclude(
        time_slot__in=Subquery(booked_timeSlot.values('time_slot'))) & TimeSlotTable.objects.filter(
        available=True).order_by('id')
    return JsonResponse(list(time_slots.values('time_slot')), safe=False)


"AJAX FUNCTION TO GET CORRESPONDING PRICE ACCORDING TO TIME SLOT SELECTED "


def load_price(request):
    time_id = request.GET.get('time_id')
    time_object = TimeSlotTable.objects.filter(time_slot=time_id)
    for data in time_object:
        price = data.price
    return JsonResponse(price, safe=False)
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
    # return render(request, 'persons/city_dropdown_list_options.html', {'cities': price})


"ORDER HISTORY"


def order_history(request):
    userid = request.session['userid']
    first_name = User.objects.get(id=userid)
    items = BookingTable.objects.filter(userid=userid).order_by('-id')
    if items is not None:
        for orders in items:
            if orders.id is not None:
                return render(request, 'Order_history.html', {'orders': items, 'user': first_name})
        messages.info(request, 'Not Yet Booked Anything!!!')
        return render(request, 'Order_history.html', {'user': first_name})


"CANCEL ORDER"


def cancel_order(request, oid):
    booked_item = BookingTable.objects.filter(id=oid).update(book_status='cancelled')
    cancelled = True
    return redirect(order_history)


def home(request):
    userid = request.session['userid']
    first_name = User.objects.get(id=userid)
    return render(request, 'home.html', {'user': first_name})
