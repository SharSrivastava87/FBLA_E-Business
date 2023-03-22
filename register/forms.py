# Import necessary modules
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Define the RegisterForm class, which is a subclass of UserCreationForm
class RegisterForm(UserCreationForm):
    # Define the email field for the form
    email = forms.EmailField()

    # Define the Meta class, which provides additional information about the form
    class Meta:
        # Set the model to User, which is the built-in user model in Django
        model = User
        # Set the fields that will be displayed on the form
        fields = ["username", "email", "password1", "password2"]
