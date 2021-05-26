from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200,default = '',null = True)
    writer = models.CharField(max_length=100,default = '',null = True)
    image = models.ImageField(upload_to = 'images/',default = '',null = True)
    description = models.CharField(max_length=100 ,default = '',null = True)
    pub_date = models.DateTimeField(default = '',null = True)
    body = models.TextField(default = '',null = True)

    def __str__(self):
        return self.title