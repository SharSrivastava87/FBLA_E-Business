# Import necessary modules from Django
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView

# Import check_availability function from a module
from Homepage.Booking_Functions.availability import check_availability
from .forms import AvailabilityForm
# Import models and forms from this app
from .models import Room, Booking


# Import messages for use in logout_view
from django.contrib import messages
# Define views
# Display a list of all available rooms
class RoomList(ListView):
    model = Room
    template_name = "index.html"


# Display a list of all bookings
class BookingList(ListView):
    model = Booking
    template_name = "MapAPI.html"


# Display homepage
def my_view(request):
    return render(request, 'index1.html')


# Display terms and policy page
def terms(request):
    return render(request, 'Terms&policy.html')

def boookedout(request):
    return render(request, 'booked_out.html')
# Allow user to book a room if available
from django.contrib import messages

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            # If we've found enough available rooms, we don't need to check the rest of the rooms
            if len(available_rooms) == data['num_rooms']:
                break
            # Check if the room is available during the requested dates
            if check_availability(room, data['check_in'], data["check_out"]):
                available_rooms.append(room)
        # If we found enough available rooms, create a booking for each room
        if len(available_rooms) == data['num_rooms']:
            for room in available_rooms:
                booking = Booking.objects.create(
                    user=self.request.user,
                    room=room,
                    check_in=data['check_in'],
                    check_out=data['check_out'],
                    points = 100

                )
                booking.save()
                return redirect('/checkout')


        else:


            return redirect('/Booked_Out')


# Allow user to log out and display a success message
def logout_view(request):
    logout(request)
    return redirect('/')


# Display checkout page
def checkout_view(request):
    bookings = request.user.bookings.filter(completed=False)
    total = 0
    for booking in bookings:
        total += booking.room.price
    total *= 1.08
    total = round(total, ndigits=2)
    booked_complete = request.user.bookings.filter().update(completed=True)
    return render(request, 'Checkout.html', {"bookings": bookings, "total_cost": total})


