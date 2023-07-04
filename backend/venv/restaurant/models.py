from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    no_of_guests = models.IntegerField(null=True, default=0, verbose_name='Number of Guests')
    booking_date = models.DateTimeField(verbose_name='Booking Date')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bookings'


class Menu(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    inventory = models.IntegerField(default=0, verbose_name='Inventory')

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    class Meta:
        verbose_name_plural = 'Menus'