from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

# Vista temporal de prueba para la página principal
def home_view(request):
    return HttpResponse("<h1>¡Bienvenido a mi proyecto en Render! 🚀 Todo funciona a la perfección.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
]