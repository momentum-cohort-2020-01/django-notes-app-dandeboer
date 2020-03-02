from django import forms

from .models import Note

class PostForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'body')