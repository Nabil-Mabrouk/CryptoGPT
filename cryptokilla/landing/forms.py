from django import forms
from .models import Config

class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'  # You can customize this based on which fields you want to allow editing
