from django.urls import path
from .views import BookingList, RoomList, BookingView
app_name = 'Homepage'

urlpatterns=[
    path('room_list/', RoomList.as_view(), name = 'RoomList'),
    path('', BookingList.as_view(), name = 'BookingList'),
    path('book/', BookingView.as_view(), name='booking_view')
]