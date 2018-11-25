from django import forms
import datetime
from django.contrib.admin.widgets import AdminDateWidget

class LoginForm(forms.Form):
    rut= forms.CharField(label='',
                        max_length=10,
                        widget=forms.TextInput(attrs={'class':'form-control',
                                                    'placeholder':'RUT',
                                                    'id':'inputUser'}))
    clave= forms.CharField(label='',
                        widget=forms.PasswordInput(attrs={'class':'form-control',
                                                    'placeholder': 'Contraseña',
                                                    'id': 'inputPassword'}))
class CoevForm(forms.Form):
    nombre=forms.CharField(label='',
                        max_length=10,
                        widget=forms.TextInput(attrs={'class':'form-control',
                                                    'placeholder':'ej: Tarea 1, Presentación 3, etc.',
                                                    'id':'titleCoev'}))
    fecha=forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)   
    hora_inicio = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    hora_termino=forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    fecha_fin=forms.DateField(
    widget=forms.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)