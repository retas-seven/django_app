from django import forms
from.models import Message,Group,Friend,Good
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    '''
    Messageのフォーム（未使用）
    '''
    class Meta:
        model = Message
        fields = ['owner','group','content']

class GroupForm(forms.ModelForm):
    '''
    Groupのフォーム（未使用）
    '''
    class Meta:
        model = Group
        fields = ['owner', 'title']

class FriendForm(forms.ModelForm):
    '''
    Friendのフォーム（未使用）
    '''
    class Meta:
        model = Friend
        fields = ['owner', 'user', 'group']

class GoodForm(forms.ModelForm):
    '''
    Goodのフォーム（未使用）
    '''
    class Meta:
        model = Good
        fields = ['owner', 'message']

class SearchForm(forms.Form):
    '''
    検索フォーム
    '''
    search = forms.CharField(max_length=100)

class GroupCheckForm(forms.Form):
    '''
    Groupのチェックボックスフォーム
    '''
    def __init__(self, user, *args, **kwargs):
        super(GroupCheckForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.MultipleChoiceField(
            choices=[(item.title, item.title) for item in Group.objects.filter(owner__in=[user,public])],
            widget=forms.CheckboxSelectMultiple(),
        )

class GroupSelectForm(forms.Form):
    '''
    Groupの選択メニューフォーム
    '''
    def __init__(self, user, *args, **kwargs):
        super(GroupSelectForm, self).__init__(*args, **kwargs)
        self.fields['groups'] = forms.ChoiceField(
            choices=[('-','-')] + [(item.title, item.title) for item in Group.objects.filter(owner=user)],
        )

class FriendsForm(forms.Form):
    '''
    Friendのチェックボックスフォーム
    '''
    def __init__(self, user, friends=[], vals=[], *args, **kwargs):
        super(FriendsForm, self).__init__(*args, **kwargs)
        self.fields['friends'] = forms.MultipleChoiceField(
            choices=[(item.user, item.user) for item in friends],
            widget=forms.CheckboxSelectMultiple(),
            initial=vals
        )

class CreateGroupForm(forms.Form):
    '''
    Group作成フォーム
    '''
    group_name = forms.CharField(max_length=50)

class PostForm(forms.Form):
    '''
    投稿フォーム
    '''
    content = forms.CharField(max_length=500, \
            widget=forms.Textarea)
    
    def __init__(self, user, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        public = User.objects.filter(username='public').first()
        self.fields['groups'] = forms.ChoiceField(
            choices=[('-','-')] + [(item.title, item.title) \
                     for item in Group.objects. \
                     filter(owner__in=[user,public])],
        )
