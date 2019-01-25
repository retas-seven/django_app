from django.views import View
from django.shortcuts import render
from shohin.services.shohin_toroku_service import ShohinTorokuService

class ShohinTorokuView(View):
    def get(self, request, *args, **kwargs):
        '''
        商品登録画面初期表示処理
        '''
        condition = {}
        params = ShohinTorokuService().retrieveShohin(condition)

        return render(request, 'shohin/shohin_toroku.html', params)
