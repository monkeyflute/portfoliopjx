from django.db import models

class Blog(models.Model):
    #title
    title = models.CharField(max_length=100)
    #date
    timestamp= models.DateTimeField()
    #body
    body = models.TextField()
    #image
    image = models.ImageField(upload_to='images/')
