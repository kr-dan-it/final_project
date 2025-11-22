from django.contrib import admin
from .models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ('predictions', 'elevation', 'soil_code', 'sepal_length',
                    'sepal_width', 'petal_length', 'petal_width',
                    'petal_curvature', 'leaf_area_cm2')

admin.site.register(Data, DataAdmin)
