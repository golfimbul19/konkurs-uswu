from django import forms

from .models import Topic, Entry
from ckeditor.widgets import CKEditorWidget

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['topic', 'header', 'image', 'budget', 'text',  'rich_text']
        labels = {'topic':'Категорія проекту','header':'Назва проекту', 'image':'Посилання на головне фото проекту', 'budget': 'Бюджет проекту, грн', 'text': 'Короткий опис проекту',  'rich_text': 'Детальний опис проекту'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}), 'image': forms.Textarea(attrs={'cols': 80, 'rows': 1}), 'rich_text': CKEditorWidget()}