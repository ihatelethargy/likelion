from django.db import models


# Create your models here.
## model 설계
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()


    ## 여기에 str 넣어준다.
    def __str__(self):
        return self.title  

    def summary(self):
        return self.body[:100]