# Generated by Django 4.2.2 on 2023-07-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('no_of_guests', models.IntegerField(default=0, null=True, verbose_name='Number of Guests')),
                ('booking_date', models.DateTimeField(verbose_name='Booking Date')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('inventory', models.IntegerField(default=0, verbose_name='Inventory')),
            ],
            options={
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
