from django import forms
from django.core import validators
from .models import User
 
class Student(forms.ModelForm):
     
    name = forms.CharField(
            validators=[
                validators.MinLengthValidator(3, "Minimum 3 or more characters needed"),
                validators.RegexValidator(
                    regex=r'^[a-zA-Z0-9]+$',
                    message='Username must contain only alphanumeric characters.',
                ),
        ]
    )
     
    class Meta:
         model = User
         fields = ['name','email','password']
         widget={
             'name':forms.TextInput(),
             'email':forms.EmailInput(),
             'password':forms.PasswordInput(),
         }
         