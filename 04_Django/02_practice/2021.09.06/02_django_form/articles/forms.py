from django.forms import fields, widgets
from articles.models import Article
from django import forms

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows':5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please Enter your Content'
        }
    )

    class Meta:
        model = Article
        fields ='__all__'
        # exclude = ('content',)
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'title',
        #         'placeholder': 'Enter the title',
        #         'maxlength': 10,
        #     })
        # }