# 2. django form을 저장할 수 있는 파일임
from django import forms
from .models import Blog   # Blog 모델을 기반으로 form을 만들 것

#


class BlogForm(forms.Form):
    # 입력받고자하는 값을 필드 형식을 지정해 입력해두면 된다.
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    # widget 참고자료: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog       # blog title을 받음
        # 어떤 요소들을 상속받을지 지정 e.g. fields = '__all__'
        fields = ['title', 'body']
