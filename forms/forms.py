from django.forms import ModelForm
from .models import DigitalForm

class DigiForm(ModelForm):
    class Meta:
        model = DigitalForm
        fields = ['first_name', 'last_name', 'age', 'birth_place']