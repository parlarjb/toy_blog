from django import forms
from django.conf import settings

MAX_LENGTH = getattr(settings, "MAX_COMMENT_NAME_LENGTH", 128)

class CommentForm(forms.Form):
    author = forms.CharField(max_length=MAX_LENGTH)
    body = forms.CharField(widget=forms.Textarea)
    parent = forms.CharField(widget=forms.HiddenInput)
