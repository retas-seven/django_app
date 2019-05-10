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
    def __init__(self, request):
        self.request = request

    def retrieveNohin(self):
        '''
        納品一覧情報を検索する
        '''
        nohinList = (Nohin.objects
            .filter(belong_user=self.request.user.email)
            .values('id', 'nohin_date', 'nohinsaki', 'total_price', 'memo')
            .order_by('-nohin_date', '-regist_date') # 降順
        )
        return nohinList
    
    def retrieveNohinDetailList(self):
        '''
        納品詳細情報を検索する
        '''
        ret = {}
        nohinDetailList = list(NohinDetail.objects
            .filter(belong_user=self.request.user.email)
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
                .filter(belong_user=self.request.user.email)
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
                .filter(belong_user=self.request.user.email)
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
                belong_user=self.request.user.email,
                id=id,
            ).exists()
        )
        return ret

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
            company.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            company.save()

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
        nohin.belong_user = self.request.user.email
        nohin.total_price = Decimal(totalPrice) * Decimal('1.08')  # 税込額
        nohin.regist_user = self.request.user.email
        nohin.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        for detail in registDetailFormset.save(commit=False):
            detail.belong_user = self.request.user.email
            detail.regist_user = self.request.user.email
            detail.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            detail.nohin = nohin
        registDetailFormset.save()

    def deleteNohin(self, nohin_id):
        '''
        商品情報を削除する
        '''
        nohin = Nohin.objects.get(belong_user=self.request.user.email, id=nohin_id)
        nohin.delete()

    def updateNohin(self, updateNohinId, updateForm, updateDetailFormset):
        '''
        商品情報を更新する
        '''
        nohin = Nohin.objects.get(
            belong_user=self.request.user.email,
            id=updateNohinId,
        )

        # 画面で入力した納品を取得する
        nohinFormModel = updateForm.save(commit=False)
        detailList = updateDetailFormset.save(commit=False)

        totalPrice = 0
        for detail in detailList:
            totalPrice += Decimal(detail.price) * Decimal(detail.amount)

        # 画面からPOSTされたデータの他に必須のデータをセットして保存する
        nohin.nohin_date = nohinFormModel.nohin_date
        nohin.total_price = Decimal(totalPrice) * Decimal('1.08')  # 税込額
        nohin.memo = nohinFormModel.memo
        nohin.nohinsaki = nohinFormModel.nohinsaki
        nohin.update_user = self.request.user.email
        nohin.update_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        # 更新はdelete→insertとする
        NohinDetail.objects.filter(
            nohin=nohin
        ).delete()

        for detail in updateDetailFormset.save(commit=False):
            detail.belong_user = self.request.user.email
            detail.regist_user = self.request.user.email
            detail.regist_date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            detail.nohin = nohin
        updateDetailFormset.save()