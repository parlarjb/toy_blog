from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    slug = forms.SlugField()
    date = forms.DateField()
    body = forms.CharField(widget=forms.Textarea)
