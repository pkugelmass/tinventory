from django import forms
from .models import Transformation, Ministry
from taggit.models import Tag 


# Custom field class that adds an empty choice at the top of the drop-down box.
class ChoiceFieldEmpty(forms.ChoiceField):
     
     def __init__(self,*args,**kwargs):
          super(ChoiceFieldEmpty,self).__init__(*args,**kwargs)
          self.choices = [('',' ')] + self.choices

class TransformationFilterForm(forms.Form):
     
     MINISTRY_LIST = ( ( m , (m.abbrev + ' - ' + m.name) ) for m in Ministry.objects.all().order_by('abbrev') ) #remove order once migrated
     TAG_LIST = ( ( tag, tag.name ) for tag in Tag.objects.all().order_by('name') )
     
     ministry__abbrev = ChoiceFieldEmpty(choices = MINISTRY_LIST, label="Ministry", required=False)
     category = ChoiceFieldEmpty(choices = Transformation.CATEGORIES, label="Category", required=False)
     status = ChoiceFieldEmpty(choices = Transformation.STATUSES, label="Status", required=False)
     tags__name = ChoiceFieldEmpty(choices = TAG_LIST, label="Tag", required=False)