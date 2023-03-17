from django.urls import path
from .views import BookingList, RoomList, BookingView
from register.views import login_view
from . import views
app_name = 'Homepage'

urlpatterns=[
    path('', RoomList.as_view(), name = 'RoomList'),
    path('NearbyAttractions/', BookingList.as_view(), name = 'BookingList'),
    path('book/', BookingView.as_view(), name='booking_view'),
    path('Pricing/', views.my_view),
    path('login/', login_view, name='login'),

]