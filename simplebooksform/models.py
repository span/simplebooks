import os
from datetime import datetime
from django.db import models

def update_filename(instance, filename):
    year = '2014'
    path = "documents/" + year
    count = verification.objects.count()
    ext = filename.split('.')[-1]
    format = str(count) + "-" + instance.title + "-" + instance.account + "." + ext
    return os.path.join(path, format)

class verification(models.Model):
    title = models.CharField(max_length = 40)
    amount = models.IntegerField(max_length = 10)
    account = models.CharField(max_length = 40)
    tax6 = models.IntegerField(blank = True, null = True)
    tax12 = models.IntegerField(blank = True, null = True)
    tax25 = models.IntegerField(blank = True, null = True)
    timestamp = models.DateTimeField(default = datetime.now)
    invoice = models.FileField(upload_to = update_filename)
    
    def __unicode__(self):
            # Make the model readable.
            return self.title
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        