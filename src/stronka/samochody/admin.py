
from django.contrib import admin

# Register your models here.
#from .models import samochody, Wlasciciel, MarkaSamochodu
from .models import samochody, Wlasciciel, MarkaSamochodu 

# admin.register(samochody)
# class SamochodyAdmin(admin.ModelAdmin):
#     fields = ["marka", "paliwo", "wlasciciele", "opis", "cena"]

# admin.register(Wlasciciel)
# class WlascicielAdmin(admin.ModelAdmin):
#     fields = ["imie", "nazwisko"]


# admin.register(MarkaSamochodu)
# class MarkaSamochoduAdmin(admin.ModelAdmin):
#     fields = ["marka", "model"]

admin.site.register(samochody)
admin.site.register(Wlasciciel)
admin.site.register(MarkaSamochodu)