from typing import Any, Dict
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100, min_length=5)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput, min_length=8)

class RegisterForm(forms.Form):
    user_name = forms.CharField(max_length=100, min_length=4)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput, min_length=8)
    verify_password = forms.CharField(max_length=40, widget=forms.PasswordInput, min_length=8)

    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        password = cleaned_data.get("password")

        verify_password = cleaned_data.get("verify_password")
        if password != verify_password:
            self.add_error('verify_password', "Password does not match")
            self.add_error('password', "Password does not match")

        return cleaned_data