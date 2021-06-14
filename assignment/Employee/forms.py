from django import forms
from django.core.validators import MinLengthValidator
from .models import Employee


class SignupForm(forms.Form):

    username = forms.CharField(validators = [MinLengthValidator(6)])
    password = forms.CharField(widget=forms.PasswordInput(),validators = [MinLengthValidator(8)])

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'gender', 'salary', 'address']