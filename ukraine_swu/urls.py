"""Defines URL patterns"""

from django.urls import path

from . import views

app_name = 'ukraine_swu'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('people/', views.people, name='people'),
    # Detail page for a single topic.
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new entry.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    path('entry_page/<int:entry_id>/', views.entry_page, name='entry_page'),

 
]