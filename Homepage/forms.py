from django import forms
from django.forms import DateInput

class DateInput(forms.DateInput):
    input_type = 'date'
class AvailabilityForm(forms.Form):
    ROOM_Categories = (
        ('STA', 'Standard'),
        ('DEL', 'Deluxe'),
        ('SUI', 'Suite'),
    )

    room_category = forms.ChoiceField(choices=ROOM_Categories, required=True)
    check_in = forms.DateTimeField(widget=DateInput, required=True)
    check_out = forms.DateTimeField(widget=DateInput, required=True)
    num_rooms = forms.IntegerField(required=True, min_value=1)


