from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone', 'profile_picture',
            'date_of_birth', 
            'address', 'city', 'postal_code', 'emergency_contact',
            'password1', 'password2'
        ]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone', 'profile_picture',
            'date_of_birth',  
            'address', 'city', 'postal_code', 'emergency_contact',
        ]
