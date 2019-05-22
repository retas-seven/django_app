from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.forms.shohin_form import ShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin
from shohin.services.shohin_service import ShohinService


class ShohinUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        '''
        商品更新画面-初期表示処理
        '''
        kataban = request.GET['kataban']
        shohin = ShohinService(request).retrieveShohin(kataban)
        
        if not shohin:
            messages.error(request, '商品情報の取得に失敗しました。')
            return redirect(reverse('shohin_list_view'))

        params = {
            'mode': 'update',
            'form': ShohinForm(list(shohin)[0])
        }

        return render(request, 'shohin/regist.html', params)

    def post(self, request, *args, **kwargs):
        '''
        商品更新画面-更新処理
        '''
        service = ShohinService(request)
        kataban = request.POST.get('kataban')
        shohin = service.retrieveShohinModel(kataban)

        if not shohin:
            messages.error(request, '商品情報の更新に失敗しました。')
            return redirect(reverse('shohin_list_view'))

        form = ShohinForm(request.POST, instance=shohin)

        if not form.is_valid():
            params = {
                'mode': 'update',
                'form': form
            }
            return render(request, 'shohin/regist.html', params)

        # 商品情報を更新
        service.updateShohin(form)
        messages.success(request, '商品情報を更新しました。')

        # 商品一覧画面の初期表示処理へリダイレクト
        return redirect(reverse('shohin_list_view'))
