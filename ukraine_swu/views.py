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
    context = {'topic': topic,'topics': topics, 'entries': entries}
    return render(request, 'ukraine_swu/index.html', context)

def people(request):
    people = Volunteer.objects.all()
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics,'people': people}
    return render(request, 'ukraine_swu/people.html', context)

def topic(request, topic_id):
    """Категорія і проекти"""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    
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
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('ukraine_swu:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form, 'topics': topics}
    return render(request, 'ukraine_swu/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """редагувати проект."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topics = Topic.objects.order_by('date_added')
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ukraine_swu:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form, 'topics': topics}
    return render(request, 'ukraine_swu/edit_entry.html', context)

