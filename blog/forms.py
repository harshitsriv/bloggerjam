from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name')

choice_list = [item for item in choices]


class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','category', 'author', 'body', )

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Title Here'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'id':'user', 'type':'hidden'},),
            #'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

        }

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add Title Here'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

        }
