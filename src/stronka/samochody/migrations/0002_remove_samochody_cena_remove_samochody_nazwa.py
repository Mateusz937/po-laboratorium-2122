# Generated by Django 4.0.4 on 2022-06-09 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samochody',
            name='cena',
        ),
        migrations.RemoveField(
            model_name='samochody',
            name='nazwa',
        ),
    ]