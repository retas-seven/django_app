
import requests
from django.contrib.auth.models import User

class UnittestMiddleware:

    def __init__(self, get_response):
        '''
        サーバ起動時の処理
        '''
        self.get_response = get_response

        # ------------------------------
        # 単体テスト用ユーザをinsert
        # ------------------------------
        # from django.contrib.auth.models import User
        # utuserExists = (User.objects
        #     .filter(
        #         username='ut_user',
        #         email='ut_user@settings.com'
        #     ).exists()
        # )
        # print('----------------')
        # print(utuserExists)
        # print('----------------')

        # if not utuserExists: 
            # user = User.objects.create(
            #     username='ut_user@settings.com',
            #     email='ut_user@settings.com',
            #     # password='admin'
            #     # password='pbkdf2_sha256$120000$8XwkNp4C5aOZ$l03UnUdiZYisT58tC3eL6Lc5Z3/PccOaVifXGpMot6w=' # admin
            # )
            # print('----------------')
            # print(user.__dict__)
            # print('----------------')
            # user.set_password('admin')
            # user.save()
            # User.objects.create(username='ut_user', password='pass@123', email='ut_user@settings.com')


    def __call__(self, request):
        '''
        前処理
        '''
        # print('----------------')
        # print(vars(request.user))
        # print(vars(request.session))
        # print('----------------')

        # loginResponse = requests.post('http://testserver/accounts/login/', {'login': 'admin@test.com', 'password': 'admin'})
        # print('-loginResponse---------------')
        # print(loginResponse)
        # print('----------------')

        response = self.get_response(request)

        return response
