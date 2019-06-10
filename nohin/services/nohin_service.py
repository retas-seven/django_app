from app_table.models import Nohin
from app_table.models import NohinDetail
from app_table.models import Shohin
from app_table.models import Company
from decimal import Decimal, ROUND_DOWN
from datetime import datetime
from django.db.models import Sum
from django.db import connection
import json

class NohinService:
    '''
    納品画面用サービスクラス
    '''
    def __init__(self, request):
        self.request = request

    def retrieveNohin(self, nohinId):
        '''
        納品情報を検索する
        '''
        nohin = (Nohin.objects
            .filter(belong_user=self.request.user.email, id=nohinId)
            .values('id', 'nohin_date', 'nohinsaki', 'total_price', 'memo')
        )
        return nohin

    def retrieveNohinDetailList(self, nohinId):
        '''
        納品情報を検索する
        '''
        nohinDetailList = (NohinDetail.objects
            .filter(belong_user=self.request.user.email, nohin_id=nohinId)
        )
        return nohinDetailList

    def retrieveNohinModel(self, nohinId):
        '''
        納品情報を検索する
        '''
        nohin = Nohin.objects.get(belong_user=self.request.user.email, id=nohinId)
        return nohin

    def retrieveNohinDetailModelByNohin(self, nohin):
        '''
        納品情報を検索する
        '''
        nohinDetail = NohinDetail.objects.all().filter(
            belong_user=self.request.user.email, 
            nohin=nohin
        )

        return nohinDetail
    
    def retrieveNohinList(self):
        '''
        納品一覧情報を検索する
        '''
        # nohinList = (Nohin.objects
        #     .filter(belong_user=self.request.user.email)
        #     .values('id', 'nohin_date', 'nohinsaki', 'total_price', 'memo')
        #     .values('id', 'nohin_date', 'nohinsaki', 'memo')
        #     .order_by('-nohin_date', '-regist_date') # 降順
        #     .annotate(total_price = Sum('nohindetail__price * nohindetail__amount')) 
        # )

        query = '''
            select
                n.id, n.nohin_date, n.nohinsaki, n.memo, sum(d.price * d.amount) as zeinuki_total_price
            from 
                app_table_nohin as n
            left outer join
                app_table_nohindetail as d
            on
                n.id = d.nohin_id
            where
                n.belong_user = %s
            group by
                n.id, n.nohin_date, n.nohinsaki, n.memo
            order by
                n.nohin_date desc, n.regist_date desc
        '''

        def dictfetchall(cursor):
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        with connection.cursor() as cursor:
            cursor.execute(query, [self.request.user.email])
            nohinList = dictfetchall(cursor)
        
        for nohin in nohinList:
            if nohin.get('zeinuki_total_price'):
                nohin['total_price'] = (nohin.get('zeinuki_total_price') * Decimal('1.08')).quantize(Decimal('0'), rounding=ROUND_DOWN)
            else:
                nohin['total_price'] = Decimal('0')

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

        # 画面からPOSTされたデータの他に必須のデータをセットして保存する
        nohin.belong_user = self.request.user.email
        nohin.total_price = 0 # TODO:このカラムは使用しないため削除する
        nohin.regist_user = self.request.user.email
        nohin.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        for detail in detailFormset.save(commit=False):
            detail.belong_user = self.request.user.email
            detail.regist_user = self.request.user.email
            detail.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            detail.nohin = nohin
        detailFormset.save()

    def updateNohin(self, form, formset):
        '''
        納品情報を更新する
        '''
        nohin = form.save(commit=False)
        detailList = formset.save(commit=False)

        # 画面からPOSTされたデータの他に必要なデータをセットして保存する
        nohin.total_price = 0 # TODO:このカラムは使用しないため削除する
        nohin.update_user = self.request.user.email
        nohin.update_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        nohin.save()

        for detail in detailList:
            if detail.id is None:
                # 新規追加レコードの場合
                detail.belong_user = self.request.user.email
                detail.regist_user = self.request.user.email
                detail.regist_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                detail.nohin = nohin
            else:
                # 更新レコードの場合
                detail.update_user = self.request.user.email
                detail.update_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

        formset.save()
