from django.db import models

#사용자가 입력한 자가진단 데이터를 담는 곳
#판단1 + 선택 20 + 사용자아이디1 + 시간

class Post(models.Model):
    result = models.IntegerField()
    s_1 = models.IntegerField(default=-1)
    s_2 = models.IntegerField(default=-1)
    s_3 = models.IntegerField(default=-1)
    s_4 = models.IntegerField(default=-1)
    s_5 = models.IntegerField(default=-1)
    s_6 = models.IntegerField(default=-1)
    s_7 = models.IntegerField(default=-1)
    s_8 = models.IntegerField(default=-1)
    s_9 = models.IntegerField(default=-1)
    s_10 = models.IntegerField(default=-1)
    s_11 = models.IntegerField(default=-1)
    s_12 = models.IntegerField(default=-1)
    s_13 = models.IntegerField(default=-1)
    s_14 = models.IntegerField(default=-1)
    s_15 = models.IntegerField(default=-1)
    s_16 = models.IntegerField(default=-1)
    s_17 = models.IntegerField(default=-1)
    s_18 = models.IntegerField(default=-1)
    s_19 = models.IntegerField(default=-1)
    s_20 = models.IntegerField(default=-1)



    user = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
