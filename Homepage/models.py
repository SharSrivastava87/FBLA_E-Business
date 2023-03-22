from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.
# Define the Room class inheriting from Django's Model class
class Room(models.Model):
    # Tuple defining ROOM_Categories with their associated codes and names
    ROOM_Categories = (
        ('STA', 'Standard'),
        ('DEL', 'Deluxe'),
        ('SUI', 'Suite'),
    )
    # Define fields for Room class
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_Categories)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField()
    # Return a string representation of the Room object
    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
# Define fields for Booking class
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    completed = models.BooleanField(default=False)
    points = models.IntegerField(default=0)




    # Return a string representation of the Booking object
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

