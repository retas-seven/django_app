from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.forms.shohin_form import ShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin
from shohin.services.shohin_service import ShohinService


class ShohinRegistView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        商品登録画面-初期表示処理
        '''
        params = {
            'mode': 'regist',
            'form': ShohinForm()
        }
        return render(request, 'shohin/regist.html', params)

    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-登録処理
        '''
        form = ShohinForm(request.POST)

        if not form.is_valid():
            params = {
                'mode': 'regist',
                'form': form
            }
            return render(request, 'shohin/regist.html', params)
    
        service = ShohinService(request)

        # 登録済みチェック
        if service.existShohin(form.cleaned_data['kataban']):
            form.add_error('kataban', '既に登録されている型番です。未登録の型番を入力してください。')
            params = {
                'mode': 'regist',
                'form': form
            }
            return render(request, 'shohin/regist.html', params)
            
        # 商品を登録する
        service.registShohin(form)
        messages.success(request, '商品情報を登録しました。')
        
        # 商品一覧画面の初期表示処理へリダイレクト
        return redirect(reverse('shohin_list_view'))
