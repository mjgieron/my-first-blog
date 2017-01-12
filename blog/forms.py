from django import forms
from .models import Post
from .models import About


class PostForm(forms.ModelForm):
    #picture = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    class Meta:
        model = Post
        fields = ('title', 'text', 'picture')    

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('title', 'text', 'picture')



