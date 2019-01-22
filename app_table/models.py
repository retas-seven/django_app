from django.db import models

# Create your models here.

class Shohin(models.Model):
    '''
    商品
    '''
    kataban = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    zaikosu = models.IntegerField(default=-1)
    regist_date = models.DateTimeField()
    regist_user = models.CharField(max_length=50)
    update_date = models.DateTimeField()
    update_user = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}, {}, {}'.format(self.kataban, self.zaikosu, self.name)

    class Meta:
        ordering = ('kataban',)