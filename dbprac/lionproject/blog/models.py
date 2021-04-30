from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) # 제한이 있는 문자열
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField() # 제한이 없는 필드

    ## 기본적인 원래 내포하고 있는 객체가 호출 되었을때 나오는게 str이다
    ## 오버라이드 하자
    def __str__(self):
        return self.title # 이렇게하면 제목으로 볼 수 있다. (~~obejct(1)아니고)

    ## 이후 python manage.py makemigrations 생성 후 -> migrations 폴더 만들기
    ## python manage.py migrate migrations 폴더 뒤져서 수정 -< migrations 폴더에 있는 데이터베이스 적용하기
    ## id 컬럼은 이미 결정 되어있다.
    ## 테이블 완성한거 어드민에서 확인하기 -> 슈퍼유저 만들기 python manage.py createsuperuser
    ## 등록하기 admin.py
    # from  .models import Blog

    # admin.site.register(Blog)  어드민에서 add를 보면 확인가능



