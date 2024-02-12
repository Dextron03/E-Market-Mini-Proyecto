from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core import validators
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Los superusuarios deben tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Los superusuarios deben tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
    

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='correo electrónico', max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True)  # Añadido campo 'username'
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # Campos adicionales para tu usuario
    name = models.CharField(max_length=75)
    surnames = models.CharField(max_length=100)
    tel = models.CharField(max_length=11) 
    objects = MyUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']
    
    def __str__(self):
        return f"username: {self.name} |email: {self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, app_label):
        return self.is_superuser
    
class Category(models.Model):
    name_category = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length= 1500, null=True, blank=True)
    
    def __str__(self):
        return self.name_category

class Commercial(models.Model):
    title = models.CharField(max_length=75, null=False, blank=False)
    description = models.TextField(max_length=1500, blank=True, null=True)
    img = models.ImageField(upload_to="media/", default="media/profile.jpg",null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(MyUser, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    
    def __str__(self) -> str:
        return self.title
    
    