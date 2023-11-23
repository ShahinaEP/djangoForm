from django import forms
from app.models import *

class BannerFrom(forms.ModelForm):
    class Meta:
        model= BannerSection
        fields= '__all__'