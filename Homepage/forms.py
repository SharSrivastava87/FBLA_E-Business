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

    room_category = forms.ChoiceField(choices= ROOM_Categories, required=True)
    check_in = forms.DateField(widget=DateInput, required=True)
    check_out = forms.DateField(widget=DateInput, required=True)

