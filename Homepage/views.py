from django.shortcuts import HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, Booking
from .forms import AvailabilityForm, DateInput
from Homepage.Booking_Functions.availability import check_availability
from django.shortcuts import render
from django.core.mail import send_mail



# Create your views here.

class RoomList(ListView):
    model = Room
    template_name = "index.html"


class BookingList(ListView):
    model = Booking
    template_name = "MapAPI.html"



def my_view(request):
    return render(request, 'index1.html')


class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if len(available_rooms) == data['num_rooms']:
                break
            if check_availability(room, data['check_in'], data["check_out"]):
                available_rooms.append(room)

        if len(available_rooms) == data['num_rooms']:
            for room in available_rooms:
                booking = Booking.objects.create(
                    user=self.request.user,
                    room=room,
                    check_in=data['check_in'],
                    check_out=data['check_out']
                )
                booking.save()
            return HttpResponse(f'{data["num_rooms"]} room(s) booked successfully!')
        else:
            return HttpResponse('Requested number of rooms are not available!')
