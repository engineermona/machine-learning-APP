from django import forms
from .models import SocialData
class SocialForm(forms.ModelForm):
    class Meta:
        model=SocialData
        fields='gender','age','salary'