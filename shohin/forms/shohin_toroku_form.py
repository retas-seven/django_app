from django import forms
from shohin.services.shohin_toroku_service import ShohinTorokuService

class RegistShohinForm(forms.Form):
    '''
    商品登録用フォーム
    '''
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for field in self.fields.values():
            # 各入力項目に「form-control form-control-lg」のCSSを適用
            field.widget.attrs['class'] = 'form-control form-control-lg'
        # 単価、在庫数の入力項目の横幅を設定
        self.fields.get('registPrice').widget.attrs['style'] = "width: 17rem;"
        self.fields.get('registZaikosu').widget.attrs['style'] = "width: 17rem;"

    registKataban = forms.CharField(
        label='型番',
        max_length=50,
    )
    registShohinName = forms.CharField(
        label='商品名',
        max_length=50,
    )
    registPrice = forms.IntegerField(
        label='単価',
        min_value=0,
    )
    registZaikosu = forms.IntegerField(
        label='在庫数',
        min_value=0,
    )
    registMemo = forms.CharField(
        label='メモ',
        max_length=1000,
        widget=forms.Textarea,
        required=False,
    )

    def clean_registKataban(self):
        registKataban = self.cleaned_data['registKataban']
        if  ShohinTorokuService().existShohin(registKataban):
            raise forms.ValidationError('既に登録されている型番です。未登録の型番を入力し、再度登録を行ってください。')
        return registKataban

class UpdateShohinForm(forms.Form):
    '''
    商品更新用フォーム
    '''
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for field in self.fields.values():
            # 各入力項目に「form-control form-control-lg」のCSSを適用
            field.widget.attrs['class'] = 'form-control form-control-lg'
        # 単価、在庫数の入力項目の横幅を設定
        self.fields.get('updatePrice').widget.attrs['style'] = "width: 17rem;"
        self.fields.get('updateZaikosu').widget.attrs['style'] = "width: 17rem;"

    updateKataban = forms.CharField(
        label='型番',
        max_length=50,
    )
    updateShohinName = forms.CharField(
        label='商品名',
        max_length=50,
    )
    updatePrice = forms.IntegerField(
        label='単価',
        min_value=0,
    )
    updateZaikosu = forms.IntegerField(
        label='在庫数',
        min_value=0,
    )
    updateMemo = forms.CharField(
        label='メモ',
        max_length=1000,
        widget=forms.Textarea,
        required=False,
    )

    def clean_updateKataban(self):
        updateKataban = self.cleaned_data['updateKataban']

        # TODO: 排他チェック

        return updateKataban