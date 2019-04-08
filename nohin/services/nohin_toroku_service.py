from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
from app_table.models import Company
from decimal import Decimal
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
    
    def retrieveNohinDetailList(self):
        '''
        納品詳細情報を検索する
        '''
        ret = {}
        nohinDetailList = list(NohinDetail.objects
            .filter(belong_user='testuser')
            .values('nohin', 'kataban', 'price', 'amount')
        )
        for nohinDetail in nohinDetailList:
            nohinId = nohinDetail.pop('nohin')
            listByNohinId = ret.get(nohinId, [])
            listByNohinId.append(nohinDetail)
            ret[nohinId] = listByNohinId
        return json.dumps(ret)

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

    def registNohin(self, registForm, registDetailFormset):
        '''
        商品情報を登録する
        '''
        # 保存対象の納品オブジェクトを取得する（この時点ではコミットしない）
        nohin = registForm.save(commit=False)
        detailList = registDetailFormset.save(commit=False)

        totalPrice = 0
        for detail in detailList:
            totalPrice += Decimal(detail.price) * Decimal(detail.amount)

        # 画面からPOSTされたデータの他に必須のデータをセットして保存する
        nohin.belong_user = 'testuser'
        nohin.total_price = totalPrice
        nohin.regist_user = 'testuser'
        nohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        for detail in registDetailFormset.save(commit=False):
            detail.belong_user = 'testuser'
            detail.regist_user = 'testuser'
            detail.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            detail.nohin = nohin
        registDetailFormset.save()

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