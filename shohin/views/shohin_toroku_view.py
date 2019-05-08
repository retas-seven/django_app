from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from shohin.services.shohin_toroku_service import ShohinTorokuService
from shohin.forms.shohin_toroku_form import RegistShohinForm
from shohin.forms.shohin_toroku_form import UpdateShohinForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ShohinTorokuView(LoginRequiredMixin, View):
    def __initParams(self, registForm=RegistShohinForm(), updateForm=UpdateShohinForm()):
        '''
        画面表示内容の初期化
        '''
        params = ShohinTorokuService(self.request).retrieveShohin()
        params['reg'] = registForm
        params['upd'] = updateForm
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
        registForm = RegistShohinForm(request)
        if not registForm.is_valid():
            params = self.__initParams(registForm=registForm)
            # 商品登録画面へ戻った際に自動でダイアログを開くためのパラメータを設定
            params['openRegistModal'] = True
            return render(request, 'shohin/shohin_toroku.html', params)
    
        # 商品を登録する
        ShohinTorokuService(request).registShohin(registForm)
        messages.success(request, '商品情報を登録しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))

class ShohinSakujoView(View):
    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-削除処理
        '''
        # 商品を削除する
        ShohinTorokuService(request).deleteShohin(request.POST.get("kataban"))
        messages.success(request, '商品情報を削除しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))

class ShohinKoshinView(View):
    def post(self, request, *args, **kwargs):
        '''
        商品登録画面-更新処理
        '''
        updateForm = UpdateShohinForm(request)
        if not updateForm.is_valid():
            params = ShohinTorokuView().__initParams(updateForm=updateForm)
            params['openUpdateModal'] = True
            return render(request, 'shohin/shohin_toroku.html', params)

        # 商品を更新する
        ShohinTorokuService(request).updateShohin(updateForm)
        messages.success(request, '商品情報を更新しました。')

        # 商品登録画面初期表示処理へリダイレクト
        return redirect(reverse('shohin_toroku'))
