from django.shortcuts import render
from .models import About, Gallery, Service
from django.core.mail import send_mail
from .models import BookingMessage


def home(request):
    context = {
        'about': About.objects.first(),
        'gallery': Gallery.objects.all(),
        'services': Service.objects.all(),
    }
    return render(request, 'index.html', context)

def send_booking(request):
    if request.method == 'POST':
        data = request.POST
        booking = BookingMessage.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            service_type=data['service'],
            message=data['message']
        )

        # Admin Email
        send_mail(
            subject=f"New Booking: {booking.service_type}",
            message=booking.message,
            from_email='noreply@site.com',
            recipient_list=['admin@site.com']
        )

        # Auto Reply Based on Service
        replies = {
            'hosting': 'Thank you for booking event hosting.',
            'mc': 'Thank you for choosing MC services.',
            'ads': 'Your advertisement request is received.',
            'voice': 'Voice over request received.',
        }

        send_mail(
            subject="Booking Confirmation",
            message=replies.get(booking.service_type),
            from_email='noreply@site.com',
            recipient_list=[booking.email]
        )
