from django import forms
from django.core import validators

class RegistroAlumnos(forms.Form):
    
    estados = [('informatica','INFORMATICA'),
               ('administracion','ADMINISTRACION'),
               ('mecanica','MECANICA'),
               ('construccion','CONSTRUCCION')
               ]
    
    regiones = []

    alumno_nombre = forms.CharField(
        validators= [
            validators.MinLengthValidator(2),
            validators.MaxLengthValidator(30)
        ]
    )
    alumno_fono = forms.CharField(
        validators=[
        validators.MinLengthValidator(9),
        validators.MaxLengthValidator(15)
        ]
    )
    alumno_fecha_ingreso = forms.CharField(
        validators=[
            validators.MaxLengthValidator(10)
        ]
    )
    alumno_direccion = forms.CharField(
        validators=[
            validators.MaxLengthValidator(50)
        ]
    )
    alumno_carrera = forms.CharField(widget=forms.Select(choices=estados))
    alumno_observacion = forms.CharField(required=False, widget=forms.Textarea)


    alumno_nombre.widget.attrs['class'] = 'form-control'
    alumno_fono.widget.attrs['class'] = 'form-control'
    alumno_fecha_ingreso.widget.attrs['class'] = 'form-control'
    alumno_direccion.widget.attrs['class'] = 'form-control'
    alumno_carrera.widget.attrs['class'] = 'form-control'
    alumno_observacion.widget.attrs['class'] = 'form-control'

    def clean_alumno_nombre(self):
        alumno_nombre = self.cleaned_data['alumno_nombre']
