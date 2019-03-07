from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from nohin.services.nohin_toroku_service import NohinTorokuService
# from shohin.forms.nohin_toroku_form import NohinTorokuForm

class NohinTorokuView(View):
    def get(self, request, *args, **kwargs):
        '''
        納品登録画面-初期表示処理
        '''
        params = self.__initParams()
        return render(request, 'nohin/nohin_toroku.html', params)

    def __initParams(self):
        service = NohinTorokuService()
        params = {
            'nohinList': service.retrieveNohin(),
            'shohinJson': service.retrieveShohin(),
            'companyJson': service.retrieveCompany(),
        }
        return params
