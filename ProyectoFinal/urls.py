"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from App import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home, name='home'),
     path('ingresar_animal/', views.registrar_animal, name='ingresar_animal'),
     path('buscar/', views.buscar_animal, name='buscar'),
     path('resultados_busqueda/<int:id>/', views.resultados_busqueda, name='resultados_busqueda'),
     path('editar_animal/<int:animal_id>/', views.editar_animal, name='editar_animal'),
     path('contacto/', views.contacto, name='contacto'),
     path('informacion/', views.informacion, name='informacion'),
]
