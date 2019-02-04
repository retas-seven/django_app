from django import forms
from shohin.services.shohin_toroku_service import ShohinTorokuService

class ShohinTorokuForm(forms.Form):
    '''
    商品登録用フォーム
    '''
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for field in self.fields.values():
            # 各入力項目に「form-control form-control-lg」のCSSを適用
            field.widget.attrs['class'] = 'form-control form-control-lg'
        # 単価、在庫数の入力項目の横幅を設定
        self.fields.get('price').widget.attrs['style'] = "width: 170px;"
        self.fields.get('zaikosu').widget.attrs['style'] = "width: 170px;"

    kataban = forms.CharField(
        label='型番',
        max_length=50,
    )
    shohinName = forms.CharField(
        label='商品名',
        max_length=50,
    )
    price = forms.IntegerField(
        label='単価',
        min_value=0,
    )
    zaikosu = forms.IntegerField(
        label='在庫数',
        min_value=0,
    )
    memo = forms.CharField(
        label='メモ',
        max_length=1000,
        widget=forms.Textarea,
        required=False,
    )

    def is_valid(self, checkMode):
        self.checkMode = checkMode
        return super().is_valid()

    def clean_kataban(self):
        kataban = self.cleaned_data['kataban']
        existShohin = ShohinTorokuService().existShohin(kataban)
            
        if self.checkMode == 'regist':
            if existShohin:
                raise forms.ValidationError('既に登録済みの型番です。未登録の型番を入力し、再度登録を行ってください。')
        elif self.checkMode == 'update':
            # TODO: 排他チェック
            pass
        return kataban