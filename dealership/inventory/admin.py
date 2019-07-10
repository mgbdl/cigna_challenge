from django.contrib import admin

from .models import Vehicle

# Register your models here.
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'description', 'color', 'doors', 'lot_number',)
    list_display_links = ('model',)
    search_fields = ('make', 'model', 'description', 'color', 'doors', 'lot_number',)
    list_per_page = 25

admin.site.register(Vehicle, VehicleAdmin)
