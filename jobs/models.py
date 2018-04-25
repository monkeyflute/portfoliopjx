from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/') # create image object
    summary  = models.CharField(max_length = 200) # caption the above image
