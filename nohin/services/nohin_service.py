from app_table.models import Nohin
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
    