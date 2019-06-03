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

    def retrieveShohin(self, kataban):
        '''
        商品情報を検索する
        '''
        shohin = (Shohin.objects
            .filter(belong_user=self.request.user.email, kataban=kataban)
            .values('id', 'kataban', 'shohin_name', 'price', 'zaikosu', 'memo')
        )
        return shohin

    def retrieveShohinModel(self, kataban):
        '''
        商品情報を検索する
        '''
        shohin = Shohin.objects.get(belong_user=self.request.user.email, kataban=kataban)
        return shohin

    def registShohin(self, form):
        '''
        商品情報を登録する
        '''
        shohin = form.save(commit=False)
        shohin.belong_user = self.request.user.email
        shohin.regist_user = self.request.user.email
        shohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        shohin.save()

    def updateShohin(self, form):
        '''
        商品情報を更新する
        '''
        shohin = form.save(commit=False)
        shohin.update_user = self.request.user.email
        shohin.update_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
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

    def deleteShohin(self, kataban):
        '''
        商品情報を削除する
        '''
        shohin = Shohin.objects.get(belong_user=self.request.user.email, kataban=kataban)
        shohin.delete()
