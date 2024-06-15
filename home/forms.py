from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ImageField, FileInput
from home.models import Suporte

class CreateUserFom(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Usuario'
    }), label='Username')

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'email',
        'placeholder': 'Email do usuario'
    }))
    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Digite a senha'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Digite novamente a senha'
    }))

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

class SuporteImage(forms.ModelForm):

    avatar = ImageField(widget=forms.FileInput)

    class Meta:
        model = Suporte
        fields = ['imagem']

class ProfileUpdateForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Suporte
        fields = ['imagem']