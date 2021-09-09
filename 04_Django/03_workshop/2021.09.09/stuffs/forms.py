from django import forms
from django.db.models.fields.files import ImageField
from django.forms.widgets import Textarea
from .models import Stuff


class StuffForm(forms.ModelForm):
    title = forms.CharField(
        label='title',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title from-control',
                'placeholder': 'Enter the title',
            }
        ),
    )

    content = forms.CharField(
        label='conetent',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 넣어주세요',
        }
    )

    image = forms.ImageField(
        label='image',
        widget=forms.FileInput(
            attrs={
                'class': 'my-image form-control',
                'type': 'file'
            }
        ),
    )


    class Meta:
        model = Stuff
        fields = '__all__'
