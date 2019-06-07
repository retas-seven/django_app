from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
from app_table.models import Company
from decimal import Decimal
from datetime import datetime
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

    def registCompany(self, companyName):
        '''
        会社名の存在有無を確認し、存在しなければ登録する
        '''
        exist = (Company.objects
            .filter(
                belong_user=self.request.user.email,
                company_name=companyName,
            ).exists()
        )

        if not exist:
            company = Company()
            company.belong_user = self.request.user.email
            company.company_name = companyName
            company.regist_user = self.request.user.email
            company.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            company.save()

    def registNohin(self, form, detailFormset):
        '''
        商品情報を登録する
        '''
        # 保存対象の納品オブジェクトを取得する（この時点ではコミットしない）
        nohin = form.save(commit=False)
        detailList = detailFormset.save(commit=False)

        totalPrice = 0
        for detail in detailList:
            totalPrice += Decimal(detail.price) * Decimal(detail.amount)

        # 画面からPOSTされたデータの他に必須のデータをセットして保存する
        nohin.belong_user = self.request.user.email
        nohin.total_price = Decimal(totalPrice) * Decimal('1.08')  # 税込額 TODO:マスタに税率を保持する
        nohin.regist_user = self.request.user.email
        nohin.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        for detail in detailFormset.save(commit=False):
            detail.belong_user = self.request.user.email
            detail.regist_user = self.request.user.email
            detail.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            detail.nohin = nohin
        detailFormset.save()
