from django.contrib import admin
from django.urls import path, include
from usuario import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('e-market/', include('usuario.urls'))
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path('signin/', views.signin, name='signin'),
    path('category/', views.category_maintenance, name='category'),
    path('commercial/', views.commercial_maintenance, name='commercial'),
    path('details/<int:id>', views.details, name='details'),
    path('my_commercials/', views.my_commercials, name='my_commercials'),
    path('delete_commercial/<int:id>', views.delete_commercial, name='delete_commercial'),
    path('edit_commercial/<int:commercial_id>', views.edit_commercial, name='edit_commercial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
