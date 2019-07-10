from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Vehicle

# Create your views here.
def inventory(request):
    if request.method == 'POST':
        make = request.POST.get('make', '')
        model = request.POST.get('model', '')
        color = request.POST.get('color', '')
        doors = request.POST.get('doors', '')
        lot_number = request.POST.get('lot_number', '')
        description = request.POST.get('description', '')

        vehicle = Vehicle(make=make, model=model, color=color, doors=doors, lot_number=lot_number, description=description)

        messages.success(request, 'Vehicle successfuly added')

        vehicle.save()
        return render(request, 'inventory/add.html')