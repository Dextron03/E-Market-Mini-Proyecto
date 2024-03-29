from django import forms
from . import models
from django.utils.html import format_html
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

class CustomUserCreationForm(UserCreationForm):
    # Agregar campos adicionales aquí
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={"class":"form-control form-control-lg mb-4"}))
    name = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={"class":"form-control form-control-lg mb-4"}))
    surnames = forms.CharField(max_length=30, label='Apellidos', widget=forms.TextInput(attrs={"class":"form-control form-control-lg mb-4"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-control-lg mb-4"}))
    tel = forms.CharField(max_length=11, label='Telefono/celular:', widget=forms.TextInput(attrs={"class":"form-control form-control-lg mb-4"}))
    password1 = forms.CharField(max_length=18, label="Contraseña", widget= forms.PasswordInput(attrs={"class":"form-control form-control-lg mb-4"}))
    password2 = forms.CharField(max_length=18, label="Confirmar contraseña", widget= forms.PasswordInput(attrs={"class":"form-control form-control-lg mb-4"}))

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
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if models.MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo electrónico ya está registrado.')
        return email
    
class CommercialForm(forms.ModelForm):
    img = forms.FileField(validators=[validators.FileExtensionValidator(["png", "jpg", "jpeg"], message='Solo puedes usar extensiones validas. (png, jpg, jpeg)')])
    
    class Meta:
        model = models.Commercial
        fields = "__all__"
        exclude = ['user']

    def clean_img(self):
        files = self.cleaned_data.get('img')
        if not files:
            raise forms.ValidationError("Por favor, selecciona al menos un archivo.")
        return files
    

class CategoryForm(forms.ModelForm):
    name_category = forms.CharField(max_length=50, label="Nombre de la categorias", widget=forms.TextInput(attrs={"class":"form-control"}))
    description = forms.CharField(max_length=1500, label="Descripcion", widget=forms.Textarea(attrs={"class":"form-control"}))
    class Meta:
        model = models.Category
        fields = "__all__"
