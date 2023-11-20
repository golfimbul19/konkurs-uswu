from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, Volunteer
from .forms import TopicForm, EntryForm


def index(request):
    """Домашня сторінка"""
    topics = Topic.objects.order_by('date_added')
    topic = Entry.objects.all()
    entries = topic.order_by('-date_added')
    people = Volunteer.objects.all()
    context = {'topic': topic,'topics': topics, 'entries': entries, 'people': people}
    return render(request, 'ukraine_swu/index.html', context)

def topic(request, topic_id):
    """Категорія і проекти"""
    topic = Topic.objects.get(id=topic_id)
    
    entries = topic.entry_set.order_by('-date_added')

    topics = Topic.objects.order_by('date_added')
    context = {'topic': topic, 'entries': entries, 'topics': topics}

    return render(request, 'ukraine_swu/topic.html', context)

#сторінка окремого проекту
def entry_page(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topics = Topic.objects.order_by('date_added')
    context = {'entry': entry, 'topics': topics}
    return render(request, 'ukraine_swu/entry_page.html', context)

@login_required    
def new_entry(request, topic_id):
    """новий проект"""
    topic = Topic.objects.get(id=topic_id)
    topics = Topic.objects.order_by('date_added')
    if request.method != 'POST':
        
        form = EntryForm()
    else:
     
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('ukraine_swu:topic', topic_id=topic_id)

 
    context = {'topic': topic, 'form': form, 'topics': topics}
    return render(request, 'ukraine_swu/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """редагувати проект."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topics = Topic.objects.order_by('date_added')

    if request.method != 'POST':
    
        form = EntryForm(instance=entry)
    else:
     
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ukraine_swu:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form, 'topics': topics}
    return render(request, 'ukraine_swu/edit_entry.html', context)

