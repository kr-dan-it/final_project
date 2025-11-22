from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['elevation', 'soil_code',
                  'sepal_length', 'sepal_width',
                  'petal_length', 'petal_width',
                  'petal_curvature', 'leaf_area_cm2']