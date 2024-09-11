from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

# Create your views here.

def home(request):
    return render(request, 'home.html')


def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = FlightForm()
    return render(request, 'registrar_vuelo.html', {'form': form})


def listar_vuelos(request):
    vuelos = Flight.objects.order_by('price')
    return render(request, 'listar_vuelos.html', {'vuelos': vuelos})


def estadisticas_vuelos(request):
    vuelos_nacionales = Flight.objects.filter(flight_type='Nacional').count()
    vuelos_internacionales = Flight.objects.filter(flight_type='Internacional').count()
    promedio_precio_nacional = Flight.objects.filter(flight_type='Nacional').aggregate(Avg('price'))['price__avg']
    return render(request, 'estadisticas_vuelos.html', {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'promedio_precio_nacional': promedio_precio_nacional
    })
