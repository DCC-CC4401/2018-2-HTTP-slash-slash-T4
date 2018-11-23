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

