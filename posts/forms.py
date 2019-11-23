from django import forms
from .models import Animal, AnimalImages


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["latinName", "reptiletype", "image", "cites", "size", "habitat", "shorttext", "behaviour", "feeding", "enclosure", "temperature", "sex", "male", "female", "breeding", "incubation",]
        # model = AnimalImages
        # fields = ["images"]
