from django.db import models

#사용자가 입력한 자가진단 데이터를 담는 곳
#판단1 + 선택 20 + 사용자아이디1 + 시간

class Post(models.Model):
    result = models.CharField(max_length=100)