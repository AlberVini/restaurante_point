from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction

from .models import Client, Restaurant, User


class UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class ClientSignUpForm(UserCreationForm):
    data_nascimento = forms.DateField(help_text='DD/MM/YYYY')
    endereco = forms.CharField(max_length=255)

    class Meta(UserCreationForm.Meta):
        model = User
        

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        Client.objects.create(user=user, data_nascimento=self.cleaned_data['data_nascimento'], endereco=self.cleaned_data['endereco'])
        #user.data_nascimento = self.cleaned_data['data_nascimento']
        #client.endereco.add(*self.cleaned_data.get('endereco'))
        
        return user


class RestaurantSignUpForm(UserCreationForm):
    cnpj = forms.CharField(max_length=18, help_text='XX.XXX.XXX/XXXX-XX')
    endereco = forms.CharField(max_length=70)

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self):
        user = super().save(commit=False)
        user.is_restaurant = True
        user.save()
        Restaurant.objects.create(user=user, cnpj=self.cleaned_data['cnpj'], endereco=self.cleaned_data['endereco']) 
        #restaurant.cnpj.add(*self.cleaned_data.get('cnpj'))
        #restaurant.endereco = self.cleaned_data['endereco']  

        return user
