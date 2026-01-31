from django import forms
from .models import UserLocation

class UserLocationForm(forms.ModelForm):
    class Meta:
        model = UserLocation
        fields = ["name", "society_landmark", "full_address", "state", "district", "pincode", "latitude", "longitude"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "society_landmark": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Society / House No / Landmark (Optional)"
            }),

            "full_address": forms.Textarea(attrs={"class": "form-control", "rows": 2, "placeholder": "Auto-filled address"}),
            "state": forms.TextInput(attrs={"class": "form-control", "placeholder": "Auto-filled state"}),
            "district": forms.TextInput(attrs={"class": "form-control", "placeholder": "Auto-filled district"}),
            "pincode": forms.TextInput(attrs={"class": "form-control", "placeholder": "Auto-filled pincode"}),
            "latitude": forms.HiddenInput(),
            "longitude": forms.HiddenInput(),
        }
