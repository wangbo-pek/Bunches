from django.db import models


GENDER_TYPE = (
    ('1', '男'),
    ('2', '女'),
)

class Person(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    age = models.IntegerField(verbose_name='年龄', default=0)
    gender = models.CharField(verbose_name='性别', max_length=16, choices=GENDER_TYPE, default='1')

    def __str__(self):
        return self.name