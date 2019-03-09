from app_table.models import Shohin
import datetime

class ShohinTorokuService:
    '''
    商品登録画面用サービスクラス
    '''

    def retrieveShohin(self):
        '''
        商品一覧情報を検索する
        '''
        shohinList = (Shohin.objects
            .filter(belong_user='testuser')
            .values('id', 'kataban', 'shohin_name', 'price', 'zaikosu', 'memo')
            .order_by('kataban')
        )
        
        ret = {
            'shohinList': shohinList,
        }
        return ret
    
    
    def existShohin(self, kataban):
        '''
        商品の存在有無を確認する
        '''
        ret = (Shohin.objects
            .filter(
                belong_user='testuser',
                kataban=kataban,
            ).exists()
        )
        return ret

    def registShohin(self, registForm):
        '''
        商品情報を登録する
        '''
        shohin = Shohin()
        shohin.belong_user = 'testuser'
        shohin.kataban = registForm.cleaned_data['registKataban']
        shohin.shohin_name = registForm.cleaned_data['registShohinName']
        shohin.price = registForm.cleaned_data['registPrice']
        shohin.zaikosu = registForm.cleaned_data['registZaikosu']
        shohin.memo = registForm.cleaned_data['registMemo']
        shohin.regist_user = 'testuser'
        shohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        shohin.save()

    def deleteShohin(self, kataban):
        '''
        商品情報を削除する
        '''
        shohin = Shohin.objects.get(belong_user='testuser', kataban=kataban)
        shohin.delete()

    def updateShohin(self, updateForm):
        '''
        商品情報を更新する
        '''
        shohin = Shohin.objects.get(
            belong_user='testuser',
            kataban=updateForm.cleaned_data['updateKataban'],
        )

        shohin.shohin_name = updateForm.cleaned_data['updateShohinName']
        shohin.price = updateForm.cleaned_data['updatePrice']
        shohin.zaikosu = updateForm.cleaned_data['updateZaikosu']
        shohin.memo = updateForm.cleaned_data['updateMemo']
        shohin.update_user = 'testuser'
        shohin.update_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        shohin.save()