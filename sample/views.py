from django.shortcuts import render
from django.http import request,HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'sample/index.html',{'form':PersonForm()})

def save(request):
    saved=False
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid:
            person = Person()
            person.name = form.cleaned_data['name'] 
            person.age= form.cleaned_data['age']
            person.address = form.cleaned_data['address']

            person.save()
            saved=True
        return HttpResponse('data saved')     

        