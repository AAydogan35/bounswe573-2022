from django import forms
from .models import Post, Comment
from tinymce.widgets import TinyMCE

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=TinyMCE(attrs={
            'rows': '3',
            'placeholder': 'Add content'
        })
    )

    class Meta:
        model = Post
        fields = ['body']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=TinyMCE(attrs={
            'rows': '3',
            'placeholder': 'Add content'
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']