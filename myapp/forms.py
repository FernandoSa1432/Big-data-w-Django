from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    #Aqui podemos personalizar el formulario de autenticacion en caso de ser necesario
    pass

