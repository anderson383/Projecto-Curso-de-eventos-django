from django import forms
from .models import User
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de Usuario'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email de Usuario'}),
            'password': forms.TextInput(attrs={'class':'form-control','placeholder':'Contraseña de Usuario','type':'password'})
        }
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingresa tu usuario'}))
    password = forms.CharField(max_length=30, widget= forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Ingresa una contraseña'}))