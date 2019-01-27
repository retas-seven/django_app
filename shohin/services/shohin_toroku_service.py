from app_table.models import Shohin
import datetime

class ShohinTorokuService:
    '''
    商品登録画面用サービスクラス
    '''

    def retrieveShohin(self, condition):
        '''
        商品一覧情報を検索する
        '''
        shohinList = (Shohin.objects
            .filter(belong_user=condition.get('belong_user'))
            .values('id', 'kataban', 'shohin_name', 'price', 'zaikosu')
            .order_by('kataban')
        )
        
        ret = {
            'test': 'testresult!',
            'shohinList': shohinList,
        }
        return ret
    
    def registShohin(self, form):
        '''
        商品情報を登録する
        '''
        shohin = Shohin()
        shohin.belong_user = 'testuser'
        shohin.kataban = form.cleaned_data['kataban']
        shohin.shohin_name = form.cleaned_data['shohinName']
        shohin.price = form.cleaned_data['price']
        shohin.zaikosu = form.cleaned_data['zaikosu']
        shohin.memo = form.cleaned_data['memo']
        shohin.regist_user = 'testuser'
        shohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        shohin.save()

