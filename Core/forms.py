from django import forms
from django.utils.timezone import now
from .models import *


class DateRangeForm(forms.Form):
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="من تاريخ", initial=now().date().replace(day=1).isoformat())
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="إلي تاريخ", initial=now().date().isoformat())


class LoginForm(forms.Form):
    username = forms.TextInput()
    password = forms.PasswordInput()


class PermissionsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['is_superuser', 'user_permissions']


class UserDisableForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'is_active',
        ]


class PasswordResetForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'password',
        ]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'username',
            'password',
            'phone_number',
            'email',
            'instance',
            'is_superuser',
            'is_staff',
            'user_permissions',
        ]
        labels = {
            'first_name': 'الإسم',
            'is_staff': 'موظف',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'instance': forms.HiddenInput(),
        }


class DisableForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'is_active',
        ]


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
