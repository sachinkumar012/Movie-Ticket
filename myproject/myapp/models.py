from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    screen_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} - {self.screen_name} - {self.date_time}"

    def available_seats(self):
        booked_seats = self.bookings.filter(status='booked').values_list('seat_number', flat=True)
        return [seat for seat in range(1, self.total_seats + 1) if seat not in booked_seats]

class Booking(models.Model):
    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    seat_number = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('show', 'seat_number', 'status')  # Prevent double booking for active bookings

    def __str__(self):
        return f"{self.user.username} - {self.show} - Seat {self.seat_number} - {self.status}"
