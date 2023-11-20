"""Defines URL patterns"""

from django.urls import path

from . import views

app_name = 'ukraine_swu'
urlpatterns = [
    # Домашня
    path('', views.index, name='index'),
    
    # Сторінка категорії
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    # Сторінка нового проекту
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Сторінка редагування проекту
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #Сторінка проекту
    path('entry_page/<int:entry_id>/', views.entry_page, name='entry_page'),

 
]