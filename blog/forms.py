from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    #picture = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    class Meta:
        model = Post
        fields = ('title', 'text', 'picture')    




