# Generated by Django 4.0.5 on 2022-06-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0002_remove_samochody_cena_remove_samochody_nazwa'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochody',
            name='cena',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]