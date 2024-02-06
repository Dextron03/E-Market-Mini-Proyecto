from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from . import forms

# Create your views here.
def signup(request):
    
    return render(request, "forms/signup.html", {"form":forms.CustomUserCreationForm})