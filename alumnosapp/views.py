from django.shortcuts import render
from alumnosapp import forms
from alumnosapp.models import Alumnos

# Create your views here.
def index(request):
    return render(request, 'index.html')

def formulario(request):
    form = forms.RegistroAlumnos()
    data = {'form' : form}
    if request.method == 'POST':
        form = forms.RegistroAlumnos(request.POST)
        if form.is_valid():
            print('formulario OK')
    return render(request, 'alumnos_form.html', data)

def lista(request):
    alumno= Alumnos.objects.all()
    data = {'alumno' : alumno}
    return render(request, 'alumnos_list.html', data)