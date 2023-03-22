# Import necessary modules and views from other apps
from django.urls import path
from .views import BookingList, RoomList, BookingView
from register.views import login_view
from . import views

# Define the app namespace
app_name = 'Homepage'

# Define the URL patterns for the Homepage app
urlpatterns=[
    # Define the URL pattern for the RoomList view
    path('', RoomList.as_view(), name='RoomList'),
    # Define the URL pattern for the BookingList view
    path('NearbyAttractions/', BookingList.as_view(), name='BookingList'),
    # Define the URL pattern for the BookingView view
    path('book/', BookingView.as_view(), name='booking_view'),
    # Define the URL pattern for the my_view view
    path('Pricing/', views.my_view),
    # Define the URL pattern for the login view
    path('login/', login_view, name='login'),
    # Define the URL pattern for the terms view
    path('Terms&Conditions/', views.terms),
    # Define the URL pattern for the logout_view view
    path('logout_user', views.logout_view, name='1234'),
    # Define the URL pattern for the checkout_view view
    path('checkout/', views.checkout_view),
]
