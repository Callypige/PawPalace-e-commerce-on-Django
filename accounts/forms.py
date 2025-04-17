from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone', 'profile_picture',
            'date_of_birth', 
            'address', 'city', 'postal_code', 'emergency_contact',
            'password1', 'password2'
        ]

class CustomUserChangeForm(UserChangeForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone', 'profile_picture',
            'date_of_birth',  
            'address', 'city', 'postal_code', 'emergency_contact',
        ]
