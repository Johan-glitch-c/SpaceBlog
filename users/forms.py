from django import forms
from .pydantic_schema import UserForm
from django.core.exceptions import ValidationError as DjangoValidationError
from pydantic import ValidationError as PydanticValidationError


class User_Form(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(label='Repeat Password',widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password'}))


    def clean(self):
        cleaned_data=super().clean()


        try:
            UserForm(**cleaned_data)

        except PydanticValidationError as e:
            for error in e.errors():
                field_name=error['loc'][0]
                message=error['msg']
                self.add_error(field_name, message)

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))