from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['topic', 'header', 'image', 'budget', 'text', 'full_text', 'rich_text']
        labels = {'topic':'Категорія проекту','header':'Назва проекту', 'image':'Посилання на фото проекту', 'budget': 'Бюджет проекту, грн', 'text': 'Короткий опис проекту', 'full_text':'Детальний опис проекту', 'rich_text': 'Форматований текст'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80}), 'image': forms.Textarea(attrs={'cols': 80, 'rows': 1}), 'full_text': forms.Textarea(attrs={'cols': 80}), 'rich_text': forms.Textarea(attrs={'class': 'ckeditor'})}