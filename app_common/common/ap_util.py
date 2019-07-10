
class ApUtil():
    @classmethod
    def getSourceAddr(cls, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META and request.META.get('HTTP_X_FORWARDED_FOR'):
            ret = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
        else:
            ret = request.META.get('REMOTE_ADDR', '')
        return ret
