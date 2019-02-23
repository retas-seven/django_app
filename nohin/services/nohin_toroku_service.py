from app_table.models import Nohin
from app_table.models import NohinDetail
import datetime

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
            .values('id', 'nohin_date', 'total_price', 'memo')
            .order_by('-nohin_date') # 降順
        )
        
        ret = {
            'nohinList': nohinList,
        }
        return ret
    
    
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