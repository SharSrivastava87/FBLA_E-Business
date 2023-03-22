# Importing forms from Django
from django import forms

# Defining a custom form widget for date input
class DateInput(forms.DateInput):
    input_type = 'date'

# Defining the AvailabilityForm class that extends Django's Form class
class AvailabilityForm(forms.Form):
    # Defining a tuple of ROOM_Categories with short and long names
    ROOM_Categories = (
        ('STA', 'Standard'),
        ('DEL', 'Deluxe'),
        ('SUI', 'Suite'),
    )

    # Defining the fields for the form
    room_category = forms.ChoiceField(choices=ROOM_Categories, required=True) # A drop-down menu with the ROOM_Categories choices
    check_in = forms.DateTimeField(widget=DateInput, required=True) # A date picker widget for the check-in date
    check_out = forms.DateTimeField(widget=DateInput, required=True) # A date picker widget for the check-out date
    num_rooms = forms.IntegerField(required=True, min_value=1) # An integer field for the number of rooms required



