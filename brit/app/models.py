from django.db import models

# Create your models here.

from django.db import models

# dynamicformapp/models.py
from django.db import models

class DynamicFormData(models.Model):
    item = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)


    def __str__(self):
        return self.item


# models.py
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name




    

