from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.ensemble import RandomForestClassifier
import joblib

SOIL = (
    (0, 'Clay'),
    (1, 'Loamy'),
    (2, 'Sandy')
)
# Create your models here.
class Data(models.Model):
    elevation = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(300.0)], null=True)
    soil_code = models.PositiveIntegerField(choices=SOIL, null=True)
    sepal_length = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    sepal_width = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    petal_length = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    petal_width = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], null=True)
    petal_curvature = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(20.0)], null=True)
    leaf_area_cm2 = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True)
    predictions = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/iris_extended_model.joblib')
        self.predictions = ml_model.predict([[self.elevation, self.soil_code, self.sepal_length,
                           self.sepal_width, self.petal_length, self.petal_width,
                           self.petal_curvature, self.leaf_area_cm2]])
        return super().save(*args, *kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Iris {self.predictions}"

