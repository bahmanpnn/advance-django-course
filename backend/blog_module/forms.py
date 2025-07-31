from django import forms
from .models import Post


# class PostForm(forms.Form):
#     name=forms.CharField()
#     message=forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content", "status", "category", "published_date"]


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status", "category", "published_date"]
