from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
from app_table.models import Company
from decimal import Decimal
import datetime
import json

class NohinService:
    '''
    納品画面用サービスクラス
    '''
    def __init__(self, request):
        self.request = request

    def retrieveNohinList(self):
        '''
        納品一覧情報を検索する
        '''
        nohinList = (Nohin.objects
            .filter(belong_user=self.request.user.email)
            .values('id', 'nohin_date', 'nohinsaki', 'total_price', 'memo')
            .order_by('-nohin_date', '-regist_date') # 降順
        )
        return nohinList

    def deleteNohin(self, nohinId):
        '''
        納品情報を削除する
        '''
        nohin = Nohin.objects.get(belong_user=self.request.user.email, id=nohinId)
        nohin.delete()

    def retrieveShohin(self):
        '''
        登録画面で選択できる商品情報を検索する
        '''
        shohinJson = json.dumps(
            list(Shohin.objects
                .filter(belong_user=self.request.user.email)
                .values('kataban', 'shohin_name', 'zaikosu', 'price')
                .order_by('kataban')
            )
        )
        return shohinJson

    def retrieveCompany(self):
        '''
        登録画面で選択できる取引先情報を検索する
        '''
        companyJson = json.dumps(
            list(Company.objects
                .filter(belong_user=self.request.user.email)
                .values('company_name')
                .order_by('company_name')
            )
        )
        return companyJson