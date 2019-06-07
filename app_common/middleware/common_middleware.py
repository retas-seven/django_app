from logging import getLogger
import sys
import traceback


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

    def __outLog(self, request, logMessage):
        '''
        リクエストごとのログを出力する
        '''
        self.logger.info(
            logMessage,
            extra={
                'user': request.user.email,
                'url': request.build_absolute_uri(),
            }
        )