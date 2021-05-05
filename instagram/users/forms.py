from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CustomProfileForm(forms.Form):
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(max_length=500, required=False)


class CustomPost(forms.Form):
    image = forms.ImageField(required=True)
    description = forms.CharField(max_length=500, required=False)


class CommentForm(forms.Form):
    textCom = forms.CharField(max_length=500)
