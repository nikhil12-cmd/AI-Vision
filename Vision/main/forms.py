from django import forms 
from .models import *
  
class NumberPlateForm(forms.ModelForm): 
  
    class Meta: 
        model = NumberPlate 
        fields = ['plate_image'] 