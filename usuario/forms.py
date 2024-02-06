from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Agregar campos adicionales aquí
    name = forms.CharField(max_length=30)
    surnames = forms.CharField(max_length=30)
    email = forms.EmailField()

    class Meta:
        model = models.MyUser
        fields = ['username', 'name', 'surnames', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"]
        user.surnames = self.cleaned_data["surnames"]
        user.email = self.cleaned_data["email"]
        user.tel = self.cleaned_data["tel"]
        if commit:
            user.save()
        return user