from django.urls import path
from . views import DigitalForm_data, create_form


urlpatterns = [
     path('data', DigitalForm_data, name = 'd_data'),
     path('data/form', create_form ,name = 'Create_form'),
]