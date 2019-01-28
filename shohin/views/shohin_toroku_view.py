from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import ShohinTorokuForm

class ShohinTorokuView(View):
    def __initParams(self, form=ShohinTorokuForm()):
        params = ShohinTorokuService().retrieveShohin({'belong_user': 'testuser'})
        params['form'] = form
        return params

    def get(self, request, *args, **kwargs):
        '''
        商品登録画面初期表示処理
        '''
        params = self.__initParams()
        return render(request, 'shohin/shohin_toroku.html', params)

    def post(self, request, *args, **kwargs):
        '''
        商品登録画面登録処理
        '''
        form = ShohinTorokuForm(request.POST)
        if not form.is_valid():
            params = self.__initParams(form)
            return render(request, 'shohin/shohin_toroku.html', params)
    
        # 商品を登録する
        ShohinTorokuService().registShohin(form)
        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('ShohinToroku'))
