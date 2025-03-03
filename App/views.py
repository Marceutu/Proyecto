from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AnimalForm
from .models import Animal
from django.http import Http404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.urls import reverse  


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
    return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

def registrar_animal(request):
    animal_form = AnimalForm()

    if request.method == 'POST':
        animal_form = AnimalForm(request.POST)
        if animal_form.is_valid():
            animal_form.save()
            messages.success(request, "Datos del animal guardados exitosamente.")
            return redirect('ingresar_animal')

    return render(request, 'core/ingresar_animal.html', {'animal_form': animal_form})




def home(request):
    return render(request, 'index.html')


def contacto(request):
    return render(request, 'contacto.html')

def informacion(request):
    return render(request, 'informacion.html')



def buscar_animal(request):
    if request.method == 'GET' and 'busqueda' in request.GET:
        busqueda = request.GET.get('busqueda', '').strip()  

        if not busqueda:  
            return render(request, 'core/buscar.html', {'mensaje': 'Ingrese un ID o código antes de buscar'})

        try:
            if busqueda.isdigit():  
                animal = Animal.objects.get(id=busqueda)
            else:  
                animal = Animal.objects.get(codigo_registro=busqueda)

            return redirect(reverse('resultados_busqueda', args=[animal.id]))

        except Animal.DoesNotExist:
            return render(request, 'core/buscar.html', {'mensaje': 'Animal no encontrado'})

    return render(request, 'core/buscar.html')  

                                               
def resultados_busqueda(request, id):
    try:
        # Buscar el animal por ID
        animal = Animal.objects.get(id=id)
        return render(request, 'core/resultados_busqueda.html', {'animal': animal})
    except Animal.DoesNotExist:
        return render(request, 'core/error.html', {'mensaje': 'Animal no encontrado'})



def editar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('resultados_busqueda', id=animal.id)  
    else:
        form = AnimalForm(instance=animal)

    return render(request, 'core/editar_animal.html', {'form': form, 'animal': animal})
