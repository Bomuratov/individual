from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User

from shop.bulma_mixin import BulmaMixin


class SingUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Create username')
    email = forms.EmailField(label='Write your email address')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Write username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Write password')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    username = forms.CharField(label='User name')
    email = forms.EmailField(label='Your email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ResetPasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label='Old password')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Creat new password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat new password')

    class Meta:
        models = User
        fields = ['old_password', 'new_password1', 'new_password2']
