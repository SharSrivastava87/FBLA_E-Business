# Import required modules
from django.urls import path
from register.views import login_view

# Set app name
app_name = 'register'

# Define URL patterns for the register app
urlpatterns=[
    path('login/', login_view, name='login'),
]
