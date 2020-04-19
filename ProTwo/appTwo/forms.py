from django import forms
from django.forms import ModelForm
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
