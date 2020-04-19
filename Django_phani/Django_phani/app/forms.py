from app import models
from app.models import User
from django import forms

class NewUser(forms.ModelForm):
    class Meta:
        Model = User
        fields = '__all__'