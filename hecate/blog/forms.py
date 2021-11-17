from django import forms
from ckeditor.widgets import CKEditorWidget
from django.db.models import fields
from .models import Answer


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget(), label="Type your answer below")

    class Meta:
        model = Answer
        fields=['answer']

