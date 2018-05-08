from django.db import models

class Blog(models.Model):
    #title
    title = models.CharField(max_length=100)
    #date
    timestamp = models.DateTimeField()
    #body
    body = models.TextField()
    #image
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.timestamp.strftime('%b %e %Y')
