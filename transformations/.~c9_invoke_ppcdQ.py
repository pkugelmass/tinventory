from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

class Transformation(models.Model):
     title = models.CharField("max_length=100)
     ministry = models.ManyToManyField('Ministry')
     description = models.TextField("High-Level Description")
     problem = models.TextField("What problem is it trying to solve?", blank=True)
     specific_orgs = models.CharField("Which specific or other organizations?", max_length=240, blank=True)
     primary_contact = models.CharField("Primary Contact", max_length=100, blank=True)
     
     CATEGORIES = (
     ('structure', 'Structure/Process'),
     ('strategy', 'Strategy/Policy'),
     ('service', 'Service Delivery'),
     ('people', 'People Development'),
     ('all', 'All of the Above'),
     )
     
     STATUSES = (
     ('direction', 'Defining Direction'),
     ('design', 'Design Stage'),
     ('implementation', 'Implementation'),
     ('sustainment', 'Sustainment'),
     ('complete', 'Past Transformation')
     )
     
     category = models.CharField(max_length=20, choices=CATEGORIES, blank=True)
     status = models.CharField(max_length=20, choices=STATUSES, blank=True)
     tags = TaggableManager()
     archived = models.BooleanField(default=False)
     
     def get_absolute_url(self):
          return reverse('transformation-detail', kwargs={'pk':self.pk})
          
     def __str__(self):
          return self.title

class Ministry(models.Model):
     abbrev = models.CharField(max_length=6)
     name = models.CharField(max_length=100)
     
     def __str__(self):
          return self.abbrev
          

