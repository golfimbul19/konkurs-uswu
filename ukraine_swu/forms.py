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
        labels = {'topic':'Категорія проекту','header':'Назва проекту', 'image':'Посилання на головне фото проекту', 'budget': 'Бюджет проекту, грн', 'text': 'Короткий опис проекту (до 120 символів)',  'rich_text': 'Детальний опис проекту'}
        widgets = {'text': forms.Textarea(attrs={'cols': 120, 'rows': 6, 'placeholder':"Коротко опишіть ваш проект (до 120 символів)", 'style':'resize:none;'}),
                   'topic':forms.Select(attrs={'cols': 50}),
                   'header': forms.Textarea(attrs={'cols': 120, 'rows': 3, 'placeholder':"Впишіть назву проекту", 'style':'resize:none;'}), 
                   'budget': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'placeholder':"Впишіть очікувану вартість", 'style':'resize:none;'}),
                   'image': forms.Textarea(attrs={'cols': 120, 'rows': 3, 'placeholder':"Вставте посилання на ілюстрацію проекту", 'style':'resize:none;'}), 
                   'rich_text': CKEditorWidget()
                   }