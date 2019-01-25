from app_table.models import Shohin

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
            .values('kataban', 'shohin_name', 'price', 'zaikosu')
            .order_by('kataban')
        )
        
        ret = {
            'test': 'testresult!',
            'shohinList': shohinList,
        }
        return ret