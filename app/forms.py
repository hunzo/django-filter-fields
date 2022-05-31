from django import forms
from .models import Entry, Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
