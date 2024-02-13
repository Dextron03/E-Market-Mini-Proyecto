from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
from . import models


# Create your views here.
@login_required
def home(request):
    User_logged = request.user
    categorys = models.Category.objects.all()
    user_ads = models.Commercial.objects.exclude(user=User_logged)
    
    # Obtiene todos los anuncios filtrados por categorías seleccionadas
    if 'category' in request.GET:
        selected_categories = request.GET.getlist('category')
        user_ads = user_ads.filter(category__id__in=selected_categories)
    
    return render(request, "index.html", {'query': user_ads, 'categorys': categorys})


def signup(request):
    form = forms.CustomUserCreationForm
    if request.method == "GET":
        return render(request, "forms/signup.html", {"form":form})
    
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user =  models.MyUser.objects.create_user(username=request.POST["username"],
                                                name=request.POST["name"],
                                                surnames=request.POST["surnames"],
                                                email=request.POST["email"],
                                                tel= request.POST["tel"],
                                                password=request.POST["password1"])
                print(request.POST)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                messages.error(request,  message='Algo a salido mal')
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "forms/signup.html", {"form":form})
        
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == "GET":
        return render(request, "forms/login.html", {"form":AuthenticationForm})
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, message="El usuario o la contraseña es incorrecta")
            return render(request, "forms/login.html", {"form":AuthenticationForm})
        else:
            login(request, user)
            return redirect("home")

@login_required
def category_maintenance(request):
    form_category = forms.CategoryForm()
    if request.method == "GET":
        return render(request, "forms/categoryform.html", {'form':form_category})
    
    if request.method == "POST":
        form_category = forms.CategoryForm(request.POST)
        if form_category.is_valid():
            form_category.save()
            messages.success(request, message='La categoria a sido creada.')
    
    return render(request, "forms/categoryform.html", {'form':form_category})

@login_required
def commercial_maintenance(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        images = request.FILES.getlist("img")  # Manejando múltiples imágenes
        price = request.POST["price"]
        category_id = request.POST["category"]

        category = models.Category.objects.get(pk=category_id)

        # Obtener el usuario actual, asumiendo que se está utilizando el sistema de autenticación de Django
        user = request.user
        
        # Crear una nueva instancia de Commercial
        new_commercial = models.Commercial.objects.create(
            title=title,
            description=description,
            price=price,
            img=images[0],
            user=user,
            category=category
        )

        # Guardar las imágenes adicionales
        for img in images:
            models.CommercialImage.objects.create(commercial=new_commercial, image=img)

        # Redirigir al usuario a la página de inicio
        return redirect('home')

    return render(request, 'forms/commercial.html', {'options': models.Category.objects.all()})

def details(request, id):
    User_logged = request.user
    ads = models.CommercialImage.objects.filter(commercial=id)
    info_ads = models.Commercial.objects.filter(id=id)
    return render(request, 'detalles.html', {'query':ads, 'info':info_ads})


# def commercial_maintenance(request):
    # form = forms.CommercialForm()
    # if request.method == "GET":
        
    #     return render(request, 'forms/commercial.html', {'form':form})
    
    # if request.method == "POST":
    #     form = forms.CommercialForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         new_commercial = form.save(commit=False)
    #         new_commercial.user = request.user
    #         new_commercial.save()
    #         return redirect('home')
    #     else:
    #         form = forms.CommercialForm()
    # return render(request, 'forms/commercial.html', {'options':models.Category.objects.all()})
    