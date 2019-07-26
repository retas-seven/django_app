# 使用する設定ファイルを指定
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shohin.tests.settings')

# Django関連のライブラリをimportしてsetup()しないと動かない
import django
from django.test import TestCase
from django.test.utils import setup_test_environment
from django.conf import settings
django.setup()
setup_test_environment()  # これをやらないと response.context['...'] で値を取得できない

import requests
from datetime import datetime
from app_table.models import Shohin

# ---------------------------------------------------------
# ■メモ
# Djangoの標準の単体テストは、下記の理由で使わないことにした。
# ・結果が見にくい
# ・テスト用DBの作成～削除が不要
# テスト実行には「green」（https://github.com/CleanCut/green）を使用する。
# ・実行方法
#   1.コマンド画面で「django_app」フォルダに移動
#   2.コマンド「green -vvv shohin/tests」を実行
# ・困ったこと
#   日本語が使えない？
# ---------------------------------------------------------

class TestShohinListView(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.URL = '/shohin/list/'

        # テストで使用するユーザのデータがあった場合、想定した結果にならないため、削除する
        cls.OTHER_DATA_EMAIL = 'other_data@ut.com'
        Shohin.objects.filter(belong_user=settings.UT_USER_EMAIL).delete()
        Shohin.objects.filter(belong_user=cls.OTHER_DATA_EMAIL).delete()

        # テストデータ
        cls.SHOHIN_LIST = [
            Shohin(
                regist_date=datetime.now(),
                regist_user=settings.UT_USER_EMAIL,
                belong_user=settings.UT_USER_EMAIL,
                kataban='TEST001',
                shohin_name='テスト１',
                zaikosu=100,
                price=10000,
                memo='メモ１',
            ),
            Shohin(
                regist_date=datetime.now(),
                regist_user=settings.UT_USER_EMAIL,
                belong_user=settings.UT_USER_EMAIL,
                kataban='TEST002',
                shohin_name='テスト２',
                zaikosu=200,
                price=20000,
                memo='メモ２',
            )
        ]
        Shohin.objects.bulk_create(cls.SHOHIN_LIST)

        # ヒットしない想定のテストデータ
        Shohin(
            regist_date=datetime.now(),
            regist_user=settings.UT_USER_EMAIL,
            belong_user=cls.OTHER_DATA_EMAIL,
            kataban='TEST001',
            shohin_name='テスト１',
            zaikosu=100,
            price=10000,
            memo='メモ１',
        ).save()
        
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        Shohin.objects.filter(belong_user=settings.UT_USER_EMAIL).delete()
        Shohin.objects.filter(belong_user=cls.OTHER_DATA_EMAIL).delete()

    def test_get(self):
        # ログインしておかないと、ViewクラスのLoginRequiredMixinで弾かれる
        self.client.login(email=settings.UT_USER_EMAIL, password=settings.UT_USER_PASS)

        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shohin/list.html')

        resultShohinList = list(response.context['shohin_list'])
        self.assertEqual(len(resultShohinList), len(self.SHOHIN_LIST))
