from django.db import models
from PIL import Image

# Create your models here.
class About(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    title = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        img = img.convert("RGB")
        img.save(self.image.path.replace('.jpg', '.webp'), 'WEBP', quality=80)

class Service(models.Model):
    SERVICE_TYPES = [
        ('hosting', 'Event Hosting'),
        ('mc', 'Master of Ceremony'),
        ('ads', 'Advertisements'),
        ('voice', 'Voice Over'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)

class BookingMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_type = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']  # FIFO

