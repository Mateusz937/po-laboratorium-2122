
from django.db import models


# Create your models here.

class RodzajePaliwa(models.TextChoices):
    LPG = ("LPG", "LPG")
    DIESEL = ("DIESEL", "diesel")
    BENZYNA = ("BENZYNA", "benzyna")
   
class MarkaSamochodu(models.Model):

    marka = models.CharField(null=False, blank=False, max_length=100)
    model = models.CharField(null=False, blank=False, max_length=100) 
    def __str__(self):
        return f"{self.marka} {self.model}"  


class Wlasciciel(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"    


class samochody(models.Model):

    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paliwo = models.CharField(choices=RodzajePaliwa.choices, max_length=10,default="LPG")
    marka = models.ForeignKey(
        to=MarkaSamochodu,
        on_delete=models.PROTECT,
        null=True
    )

    wlasciciele = models.ManyToManyField(to=Wlasciciel, related_name="samochody")
    def __str__(self):
        return f"{self.marka} of {self.wlasciciele.all()}"
    






