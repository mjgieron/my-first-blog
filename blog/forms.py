from django import forms
from .models import Post
from .models import About
from .models import Project
from .models import Other

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'picture')    

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('title', 'text', 'picture')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'text', 'picture')

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ('title', 'text', 'picture')

