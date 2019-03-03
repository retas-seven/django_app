from django.db import models

# Create your models here.
class BaseModel(models.Model):
    '''
    各モデルの共通項目
    '''
    regist_date = models.DateTimeField(verbose_name='登録日時')
    regist_user = models.CharField(verbose_name='登録ユーザ', max_length=50)
    update_date = models.DateTimeField(verbose_name='更新日時', null=True)
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
    memo = models.TextField(verbose_name='メモ', max_length=1000, null=True)

    class Meta:
        unique_together=(('belong_user', 'kataban'))
    
    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.belong_user, self.kataban, self.zaikosu, self.price, self.shohin_name)

class Company(BaseModel):
    '''
    会社
    '''
    belong_user = models.CharField(verbose_name='所属ユーザ', max_length=50)
    company_name = models.CharField(verbose_name='会社名', max_length=50)
    
    class Meta:
        unique_together=(('belong_user', 'company_name'))

    def __str__(self):
        return '{}, {}'.format(self.belong_user, self.company_name)

class Nohin(BaseModel):
    '''
    納品
    '''
    belong_user = models.CharField(verbose_name='所属ユーザ', max_length=50)
    nohin_date = models.DateField(verbose_name='納品日')
    nohinsaki = models.CharField(verbose_name='納品先', max_length=50)
    total_price = models.IntegerField(verbose_name='合計金額')
    memo = models.TextField(verbose_name='メモ', max_length=1000, null=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.belong_user, self.nohin_date, self.nohinsaki)

class NohinDetail(BaseModel):
    '''
    納品詳細
    '''
    belong_user = models.CharField(verbose_name='所属ユーザ', max_length=50)
    kataban = models.CharField(verbose_name='型番', max_length=50)
    price = models.IntegerField(verbose_name='単価')
    amount = models.IntegerField(verbose_name='数量')
    # 外部キー
    nohin = models.ForeignKey(Nohin, verbose_name='納品', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}, {}, {}, {}'.format(self.belong_user, self.kataban, self.price, self.amount)


