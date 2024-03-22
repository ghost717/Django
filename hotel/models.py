
from django.db import models
#from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Jednoosobowy'),
        ('double', 'Dwuosobowy'),
        ('suite', 'Apartament'),
        # Dodaj więcej typów pokoi zgodnie z potrzebami
    ]
    
    number = models.CharField(max_length=10, unique=True, verbose_name="Numer pokoju")
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name="Typ pokoju")
    capacity = models.IntegerField(verbose_name="Pojemność")
    beds = models.IntegerField(verbose_name="Liczba łóżek")
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena za noc")
    available = models.BooleanField(default=True, verbose_name="Dostępność")
    amenities = models.TextField(blank=True, verbose_name="Udogodnienia")

    def __str__(self):
        return f"Pokój {self.number} - {self.get_room_type_display()}"

    class Meta:
        verbose_name = "pokój"
        verbose_name_plural = "pokoje"
        
        

class Reservation(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Potwierdzona'),
        ('cancelled', 'Anulowana'),
    ]
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Zapłacono'),
        ('pending', 'Oczekuje na płatność'),
        ('cancelled', 'Anulowano płatność'),
    ]
    SERVICE_TYPE_CHOICES = [
        ('standard', 'Standardowy'),
        ('premium', 'Premium'),
        # Dodaj więcej według potrzeb
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='reservations')

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    room_type = models.CharField(max_length=50)
    room_number = models.CharField(max_length=10)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    number_of_guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS_CHOICES)
    check_in_out_verified = models.BooleanField(default=False)
    cancellation_deadline = models.DateTimeField(null=True, blank=True)
    confirmation_code = models.CharField(max_length=50, unique=True)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    special_requests = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def clean(self):
        # Sprawdzenie, czy data rozpoczęcia jest wcześniejsza niż data zakończenia
        if self.start_date and self.end_date and self.start_date >= self.end_date:
            raise ValidationError("Data rozpoczęcia musi być wcześniejsza niż data zakończenia.")

        # Możesz dodać więcej walidacji zgodnie z potrzebami

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Reservation, self).save(*args, **kwargs)

    class Meta:
        # Opcjonalnie możesz dodać dodatkowe ustawienia, np. ordering, jeśli potrzebujesz
        ordering = ['start_date']


