from django.urls import path
from . import views

urlpatterns = [
    path('booking', views.booking, name="booking"),
    path('bookTimeSlot', views.bookTimeSlot, name="bookTimeSlot"),
    path('ajax/load_available_timeSlot/', views.load_available_timeSlot, name='ajax_load_available_timeSlot'),  # AJAX
    path('ajax/load-price/', views.load_price, name='ajax_load_price'),  # AJAX
    path('order_history', views.order_history, name="order_history"),
    path('cancel_order/<int:oid>/', views.cancel_order, name="cancel_order"),
]
