# forms.py
from django import forms
from .models import Content
from ckeditor_uploader.widgets import CKEditorUploadingWidget # type: ignore

class ContentForm(forms.ModelForm):
    highlight = forms.CharField(widget=CKEditorUploadingWidget())
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Content
        fields = ['title', 'slug', 'img', 'highlight', 'content', 'tags']
