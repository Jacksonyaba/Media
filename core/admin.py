from django.contrib import admin
from .models import About, Gallery, Service, BookingMessage

admin.site.register(About)
admin.site.register(Gallery)
admin.site.register(Service)
admin.site.register(BookingMessage)

class GalleryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.has_perm('core.can_manage_gallery')
