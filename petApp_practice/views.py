from django.shortcuts import render
from .models import Vaccines, Pet

# Create your views here.
def home(request):
    pets = Pet.objects.all() #select * from pet

    return render(request, 'home.html', {'pets': pets})

def pet_details(request, id):
    specific_pet = Pet.objects.get(pk=id) # select* where primarykey is id
    return render(request, 'details.html', {'pet_details': specific_pet})
