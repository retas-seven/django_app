from django.db import models

# Create your models here.
class BaseModel(models.Model):
    '''
    各モデルの共通項目
    '''
    regist_date = models.DateTimeField(verbose_name='登録日付')
    regist_user = models.CharField(verbose_name='登録ユーザ', max_length=50)
    update_date = models.DateTimeField(verbose_name='更新日付', null=True)
    update_user = models.CharField(verbose_name='更新ユーザ', max_length=50, null=True)

    class Meta:
        abstract = True

class Shohin(BaseModel):
    '''
    商品
    '''
    belong_user = models.CharField(verbose_name='所属ユーザ', max_length=50)
    kataban = models.CharField(verbose_name='型番', max_length=50)
    shohin_name = models.CharField(verbose_name='商品名', max_length=100)
    zaikosu = models.IntegerField(verbose_name='在庫数')
    price = models.IntegerField(verbose_name='単価')
    memo = models.TextField(verbose_name='メモ', max_length=1000)
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.kataban, self.zaikosu, self.price, self.shohin_name)

    class Meta:
        unique_together=(('belong_user', 'kataban'))
