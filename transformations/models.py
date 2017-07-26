from django.db import models

class Transformation(models.Model):
     title = models.CharField(max_length=100)
     ministry = models.ManyToManyField('Ministry')
     description = models.TextField()
     
     CATEGORIES = (
          (1, 'Structure/Process'),
          (2, 'Strategy/Policy'),
          (3, 'Service Delivery'),
          )
     
     category = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
     
     def __str__(self):
          return self.title
     
class Ministry(models.Model):
     abbrev = models.CharField(max_length=6)
     name = models.CharField(max_length=100)
     
     def __str__(self):
          return self.abbrev   