from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
from app_table.models import Company
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
        return nohinList
    
    def retrieveShohin(self):
        '''
        画面のモーダルで選択できる商品情報を検索する
        '''
        shohinJson = json.dumps(
            list(Shohin.objects
                .filter(belong_user='testuser')
                .values('kataban', 'shohin_name', 'zaikosu', 'price')
                .order_by('kataban')
            )
        )
        return shohinJson

    def retrieveCompany(self):
        '''
        画面のモーダルで選択できる取引先情報を検索する
        '''
        companyJson = json.dumps(
            list(Company.objects
                .filter(belong_user='testuser')
                .values('company_name')
                .order_by('company_name')
            )
        )
        return companyJson

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
        # 保存対象の納品オブジェクトを取得する（この時点ではコミットしない）
        nohin = form.save(commit=False)
        # 画面からPOSTされたデータの他に必須のデータをセットして保存する
        nohin.belong_user = 'testuser'
        nohin.total_price = 1000
        nohin.regist_user = 'testuser'
        nohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        # nohin = Nohin()
        # nohin.belong_user = 'testuser'
        # nohin.nohin_date = registForm.cleaned_data['registNohinDate']
        # nohin.nohinsaki = registForm.cleaned_data['registNohinsaki']
        # nohin.total_price = 1000
        # nohin.memo = registForm.cleaned_data['registMemo']
        # nohin.regist_user = 'testuser'
        # nohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        # nohin.save()

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