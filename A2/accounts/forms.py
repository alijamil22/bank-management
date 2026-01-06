from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    email = forms.CharField(required=False,max_length=100)
    first_name = forms.CharField(required=False,max_length=100)
    last_name = forms.CharField(required=False,max_length=100)
    class Meta:
        Model = User
        fields = ['username','email','first_name','last_name','password1','password2']
class ProfileEdit(forms.ModelForm):
    password1 = forms.CharField(widget=forms.passwordInput(),required=False)
    password2 = forms.CharField(widget=forms.passwordInput(),required=False)
    class Meta:
        Model = User
        fields = ['first_name','last_name','email']
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get(password1)
        password2 = cleaned_data.get(password2)
        if password1 and password2:
            if password1 == password2:
                raise ValidationError("The two password fields didn't match")
            if len(password1)<8:
                raise ValidationError("his password is too short. It must contain at least 8 characters")
            return cleaned_data