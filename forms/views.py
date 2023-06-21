from django.shortcuts import render, redirect
from .models import DigitalForm
from .forms import DigiForm

def DigitalForm_data(request):
   digitalForm = DigitalForm.objects.all()
   context = {'digitalForm':digitalForm }
   return render(request, 'forms/form.html' ,context)


def create_form(request):
   if request.method == "GET":
      context = {'digiform' : DigiForm()}
      return render(request, 'forms/create_form.html' , context)
   if request.method == "POST":
      digiform = DigiForm(request.POST)
      if digiform.is_valid():
         digiform.save()
         return redirect('d_data')
      else:
         return render(request, 'forms/create_form.html' , {'digiform':digiform})