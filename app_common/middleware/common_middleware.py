from datetime import datetime, timedelta, timezone
from logging import getLogger
import sys
import traceback
from app_common.common.ap_util import ApUtil
from app_common.exception.application_exception import ApplicationException
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class CommonMiddleware:

    def __init__(self, get_response):
        '''
        サーバ起動時の処理
        '''
        # ミドルウェア用ロガー生成
        self.logger = getLogger('middleware_logger')

        self.get_response = get_response

    def __call__(self, request):
        '''
        業務処理前後の処理
        '''
        # 現在時間を設定
        # jst = timezone(timedelta(hours=+9), 'JST')
        # request.requestDate = datetime.now(jst)
        request.requestDateTime = datetime.now()

        self.__outLog(request, 'start')

        # 業務処理を実行
        response = self.get_response(request)

        self.__outLog(request, 'end')
        return response

    def process_exception(self, request, exception):
        '''
        例外発生時の処理
        '''
        print('---------------------')
        print('process_exception')
        print('---------------------')
        trc = traceback.format_exc()
        print(trc)
        print('---------------------')
        self.__outLog(request, trc)

        if type(exception) == ApplicationException:
            # アプリケーションエラーの場合はホーム画面に戻りエラーメッセージを表示する
            messages.error(request, exception.message)
            return redirect(reverse('home'))

    def __outLog(self, request, logMessage):
        '''
        リクエストごとのログを出力する
        '''
        bodyParam = dict(request.POST.lists())
        bodyParam.pop('password', None)
        bodyParam.pop('password1', None)
        bodyParam.pop('password2', None)
        bodyParam.pop('csrfmiddlewaretoken', None)

        self.logger.info(
            logMessage,
            extra={
                'addr': ApUtil.getSourceAddr(request),
                'user': request.user.email if request.user.is_authenticated else 'AnonymousUser',
                'mothod': request.method,
                'url': request.build_absolute_uri(),
                'bodyParam': bodyParam,
                'referer': request.META.get('HTTP_REFERER'),
            }
        )
    