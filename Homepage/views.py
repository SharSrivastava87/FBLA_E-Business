from django.shortcuts import HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm
from Homepage.Booking_Functions.availability import check_availability


# Create your views here.

class RoomList(ListView):
    model = Room
    template_name = 'room_list.html'


class BookingList(ListView):
    model = Booking
    template_name = 'index.html'


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data["check_out"]):
                available_rooms.append(room)
                if len(available_rooms) > 0:
                    room = available_rooms[0]
                    from django.http import request
                    booking = Booking.objects.create(
                        user=self.request.user,
                        room=room,
                        check_in=data['check_in'],
                        check_out=data['check_out']
                    )
                    booking.save()
                    return HttpResponse(booking)
            else:
                return HttpResponse('This category of rooms is booked out! Try another one')
