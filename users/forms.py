from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=50, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=50, required=False, help_text="Optional")
    email = forms.EmailField(max_length=300, help_text="Email is required")

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
