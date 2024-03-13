from django import forms
from django.contrib.auth.models import User


from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Ingrese Correo Electrónico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Ingrese su contraseña'}))


