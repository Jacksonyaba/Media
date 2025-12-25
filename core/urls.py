from django.urls import path
from .views import home, send_booking

urlpatterns = [
    path('', home, name='home'),
    path('send-booking/', send_booking, name='send_booking'),
]
