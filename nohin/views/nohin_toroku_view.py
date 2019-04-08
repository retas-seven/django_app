from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from nohin.services.nohin_toroku_service import NohinTorokuService
from nohin.forms.nohin_toroku_form import NohinForm
from nohin.forms.nohin_toroku_form import NohinUpdateForm
from nohin.forms.nohin_toroku_form import NohinDetailFormset
from nohin.forms.nohin_toroku_form import NohinDetailUpdateFormset
from app_table.models import NohinDetail

class NohinTorokuView(View):
    def get(self, request, *args, **kwargs):
        '''
        納品登録画面-初期表示処理
        '''
        params = self.__initParams()
        return render(request, 'nohin/nohin_toroku.html', params)

    def post(self, request, *args, **kwargs):
        '''
        納品登録画面-登録処理
        '''
        registForm = NohinForm(request.POST)
        registDetailFormset = NohinDetailFormset(request.POST)

        if (not registForm.is_valid()) or (not registDetailFormset.is_valid()):
            params = self.__initParams(
                registForm=registForm,
                registDetailFormset=registDetailFormset,
            )
            # 納品登録画面へ戻った際の初期処理でダイアログを開く
            params['openRegistModal'] = True
            return render(request, 'nohin/nohin_toroku.html', params)
    
        # 納品を登録する
        NohinTorokuService().registNohin(registForm, registDetailFormset)
        messages.success(request, '納品情報を登録しました。')

        # 納品登録画面初期表示処理へリダイレクト
        return redirect(reverse('nohin_toroku'))

    def __initParams(
                self, registForm=NohinForm(), 
                registDetailFormset=NohinDetailFormset(None, queryset=NohinDetail.objects.none()), 
                updateForm=NohinForm(),
                updateDetailFormset=NohinDetailUpdateFormset(None, queryset=NohinDetail.objects.none())):

        service = NohinTorokuService()
        params = {
            'nohinList': service.retrieveNohin(),
            'nohinDetailJson': service.retrieveNohinDetailList(),
            'shohinJson': service.retrieveShohin(),
            'companyJson': service.retrieveCompany(),
            'reg': registForm,
            'reglist': registDetailFormset,
            'upd': updateForm,
            'updlist': updateDetailFormset,
        }

        return params
