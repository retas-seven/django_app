from app_table.models import Shohin
import datetime

class ShohinService:
    '''
    商品管理用サービスクラス
    '''
    def __init__(self, request):
        self.request = request

    def retrieveShohinList(self):
        '''
        商品一覧情報を検索する
        '''
        shohinList = (Shohin.objects
            .filter(belong_user=self.request.user.email)
            .values('id', 'kataban', 'shohin_name', 'price', 'zaikosu', 'memo')
            .order_by('kataban')
        )
        return shohinList

    def registShohin(self, form):
        '''
        商品情報を登録する
        '''
        shohin = form.save(commit=False)
        shohin.belong_user = self.request.user.email
        shohin.regist_user = self.request.user.email
        shohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        shohin.save()
        
    def existShohin(self, kataban):
        '''
        商品の存在有無を確認する
        '''
        ret = (Shohin.objects
            .filter(
                belong_user=self.request.user.email,
                kataban=kataban,
            ).exists()
        )
        return ret