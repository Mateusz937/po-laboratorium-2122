# Generated by Django 4.0.5 on 2022-06-09 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samochody', '0003_samochody_cena'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkaSamochodu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wlasciciel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='samochody',
            name='paliwo',
            field=models.CharField(choices=[('LPG', 'LPG'), ('DIESEL', 'diesel'), ('BENZYNA', 'benzyna')], default='LPG', max_length=10),
        ),
        migrations.AddField(
            model_name='samochody',
            name='marka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='samochody.markasamochodu'),
        ),
    ]
