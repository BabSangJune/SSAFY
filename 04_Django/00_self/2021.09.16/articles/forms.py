from django import forms
from django.forms import fields
from django.forms.models import ALL_FIELDS
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'