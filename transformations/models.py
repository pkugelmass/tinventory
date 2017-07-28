from django.db import models

class Transformation(models.Model):
     title = models.CharField(max_length=100)
     ministry = models.ManyToManyField('Ministry')
     description = models.TextField("High-Level Description")
     problem = models.TextField("What problem is it trying to solve?", null=True)
     specific_orgs = models.CharField("Which specific or other organizations?", max_length=240, null=True)
     primary_contact = models.CharField("Primary Contact", max_length=100, null=True)
     
     CATEGORIES = (
     (1, 'Structure/Process'),
     (2, 'Strategy/Policy'),
     (3, 'Service Delivery'),
     )
     
     STATUSES = (
     (1, 'Defining Direction'),
     (2, 'Design Stage'),
     (3, 'Implementation'),
     )
     
     category = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
     status = models.CharField(max_length=20, choices=STATUSES, blank=True)
     
     

     
     def __str__(self):
          return self.title

class Ministry(models.Model):
     abbrev = models.CharField(max_length=6)
     name = models.CharField(max_length=100)
     
     def __str__(self):
          return self.abbrev
          

