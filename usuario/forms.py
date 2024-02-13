from django import forms
from . import models
from django.utils.html import format_html
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    # Agregar campos adicionales aquí
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={"class":"form-control"}))
    name = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={"class":"form-control"}))
    surnames = forms.CharField(max_length=30, label='Apellidos', widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    tel = forms.CharField(max_length=11, label='Telefono/celular:', widget=forms.TextInput(attrs={"class":"form-control"}))
    password1 = forms.CharField(max_length=18, label="Contraseña", widget= forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=18, label="Confirmar contraseña", widget= forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model = models.MyUser
        fields = ['username', 'name', 'surnames', 'email', 'tel', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.name = self.cleaned_data["name"]
        user.surnames = self.cleaned_data["surnames"]
        user.email = self.cleaned_data["email"]
        user.tel = self.cleaned_data["tel"]
        if commit:
            user.save()
        return user
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError(format_html('Las contraseñas no coinciden.'))
        
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        users = models.MyUser.objects.filter(username=username)
        
        if users.exists():
            raise forms.ValidationError(format_html('El usuario ya existe'))
        
        return username
    
class CommercialForm(forms.ModelForm):
    
    class Meta:
        model = models.Commercial
        fields = "__all__"
        exclude = ['user']

        

class CategoryForm(forms.ModelForm):
    name_category = forms.CharField(max_length=50, label="Nombre de la categorias", widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(max_length=1500, label="Descripcion", widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = models.Category
        fields = "__all__"