from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

# __str__ 메서드는 모델클래스의 객체의 문자열을 리턴한다.
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    