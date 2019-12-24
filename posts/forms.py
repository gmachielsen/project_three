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
        fields = ["latinName", "reptiletype", "image", "cites", "size", "habitat", "shorttext", "behaviour", "feeding", "enclosure", "lighting", "heating", "temperature", "sex", "male", "female", "breeding", "incubation", "author"]
        # model = AnimalImages
        # fields = ["images"]
