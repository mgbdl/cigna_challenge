from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.paginator import Paginator

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
        redirect('add')
    else:
        return render(request, 'inventory/add.html')

def dashboard(request):
        vehicle_list = Vehicle.objects.all()

        context = {
                'listing': vehicle_list
        }

        return render(request, 'inventory/dashboard.html', context)
