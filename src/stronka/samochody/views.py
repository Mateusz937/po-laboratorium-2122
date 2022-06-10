from django.shortcuts import render

# Create your views here.
from .models import samochody, MarkaSamochodu, Wlasciciel

def home(request):
    return render(request, "home.html")

def wszystkie_samochody(request):
    wszystkie = samochody.objects.all()

    return render(request, "wszystkie_samochody.html", {"samochody": wszystkie})

def wszystkie_marki(request):
    wszystkie = MarkaSamochodu.objects.all()

    return render(request, "wszystkie_marki.html", {"marki": wszystkie})


def wszyscy_wlasciciele(request):
    wszyscy = Wlasciciel.objects.all()

    return render(request, "wszyscy_wlasciciele.html", {"wlasciciele": wszyscy})

