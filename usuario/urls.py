from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path('signin/', views.signin, name='signin')
]
