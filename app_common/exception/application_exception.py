class ApplicationException(Exception):
    def __init__(self, message='エラーが発生したため処理を中断しました。お手数ですが再度操作を行ってください。'):
        self.message = message
