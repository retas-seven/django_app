from django.views import View
from django.shortcuts import render
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import ShohinTorokuForm

class ShohinTorokuView(View):
    def get(self, request, *args, **kwargs):
        '''
        商品登録画面初期表示処理
        '''
        condition = {'belong_user': 'testuser'}
        params = ShohinTorokuService().retrieveShohin(condition)
        params['form'] = ShohinTorokuForm()

        return render(request, 'shohin/shohin_toroku.html', params)
