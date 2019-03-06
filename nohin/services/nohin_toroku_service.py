from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
import datetime
import json

class NohinTorokuService:
    '''
    納品登録画面用サービスクラス
    '''

    def retrieveNohin(self):
        '''
        納品一覧情報を検索する
        '''
        nohinList = (Nohin.objects
            .filter(belong_user='testuser')
            .values('id', 'nohin_date', 'nohinsaki', 'total_price', 'memo')
            .order_by('-nohin_date') # 降順
        )

        # ret = {
        #     'nohinList': nohinList,
        #     'shohinJson': shohinJson,
        # }
        # return ret
        return nohinList
    
    def retrieveShohin(self):
        shohinJson = json.dumps(
            list(Shohin.objects
                .filter(belong_user='testuser')
                .values('id', 'kataban', 'shohin_name', 'zaikosu', 'price')
                .order_by('kataban')
            )
        )

        return shohinJson

    def existNohin(self, id):
        '''
        納品の存在有無を確認する
        '''
        ret = (Nohin.objects
            .filter(
                belong_user='testuser',
                id=id,
            ).exists()
        )
        return ret

    def registNohin(self, form):
        '''
        商品情報を登録する
        '''
        pass

    def deleteNohin(self, id):
        '''
        商品情報を削除する
        '''
        pass

    def updateNohin(self, form):
        '''
        商品情報を更新する
        '''
        pass