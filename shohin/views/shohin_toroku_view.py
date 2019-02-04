from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import ShohinTorokuForm

class ShohinTorokuView(View):
    def __initParams(self, form=ShohinTorokuForm(), koshinForm=ShohinTorokuForm()):
        params = ShohinTorokuService().retrieveShohin()
        params['form'] = form
        params['koshin_form'] = koshinForm
        return params

    def get(self, request, *args, **kwargs):
        '''
        商品登録画面-初期表示処理
        '''
        params = self.__initParams()
        return render(request, 'shohin/shohin_toroku.html', params)

    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-登録処理
        '''
        form = ShohinTorokuForm(request.POST)
        if not form.is_valid('regist'):
            params = self.__initParams(form)
            # 商品登録画面へ戻った際に自動でダイアログを開くためのパラメータを設定
            params['open_dialog'] = True
            return render(request, 'shohin/shohin_toroku.html', params)
    
        # 商品を登録する
        ShohinTorokuService().registShohin(form)
        messages.success(request, '商品を登録しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))

class ShohinSakujoView(View):
    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-削除処理
        '''
        # 商品を登録する
        ShohinTorokuService().deleteShohin(request.POST.get("kataban"))
        messages.success(request, '商品を削除しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))

class ShohinKoshinView(View):
    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-更新処理
        '''
        form = ShohinTorokuForm(request.POST)
        if not form.is_valid('update'):
            params = self.__initParams(form)
            return render(request, 'shohin/shohin_toroku.html', params)

        # 商品を更新する
        ShohinTorokuService().updateShohin(form)
        messages.success(request, '商品を更新しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))
