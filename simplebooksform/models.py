from datetime import datetime
from django.db import models
from django.forms import ModelForm

class verification(models.Model):
    title = models.CharField(max_length = 40)
    amount = models.IntegerField(max_length = 10)
    account = models.CharField(max_length = 40)
    tax6 = models.IntegerField(blank = True, null = True)
    tax12 = models.IntegerField(blank = True, null = True)
    tax25 = models.IntegerField(blank = True, null = True)
    timestamp = models.DateTimeField(default = datetime.now)
    
    def __unicode__(self):
            # Make the model readable.
            return self.title
            
class verification_form(ModelForm):
    # Auto generate a form to create verification models
    class Meta:
        model = verification