from django import forms
from .models import Animal, AnimalImages

class AnimalSearchForm(forms.ModelForm):
    search=forms.CharField(required=False, label="Search")
    class Meta:
        model = Animal
        fields = ["search", "latinName", "shorttext"]

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["latinName", "reptiletype", "image", "cites", "size", "habitat", "shorttext", "behaviour", "handling", "feeding", "water", "enclosure", "substrate", "lighting", "heating", "temperature", "cleaning", "sex", "male", "female", "breeding", "incubation", "health", "diseases", "author"]
        # model = AnimalImages
        # fields = ["images"]
