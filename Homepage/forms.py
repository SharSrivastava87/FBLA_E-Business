from django import forms

class AvailabilityForm(forms.Form):
    ROOM_Categories = (
        ('STA', 'Standard'),
        ('DEL', 'Deluxe'),
        ('SUI', 'Suite'),
    )
    room_category = forms.ChoiceField(choices= ROOM_Categories, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M", ])
