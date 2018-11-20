from django import forms

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

class CrearCurso(forms.Form):
    codigo=forms.CharField(max_length=15,
                           label='',
                           widget=forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder' : 'ej: CC4401',
                                                        'id':'codigoCurso'

                           }))
    OpcionesSemestres = [("Primavera", "Primavera"),
                ("Otoño", "Otoño"),
                ("Verano", "Verano")]
    semestre=forms.ChoiceField(choices=OpcionesSemestres, label='',
                        widget=forms.Select(attrs={'class':'form-control',
                                                        'id':'codigoCurso'

                        })
                        )
    año=forms.CharField(max_length=4, label='',
                        widget=forms.TextInput(attrs={'class':'form-control',
                                                        'placeholder':'ej 2018',
                                                        'id':'annoCurso'
                                                        })
                        )
    seccion=forms.IntegerField(label='',
                               widget=forms.NumberInput(attrs={'min':'1',
                                                        'class':'form-control',
                                                        'placeholder':'1',
                                                        'id':'seccionCurso'
                               }))