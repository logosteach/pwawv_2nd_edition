# project_2/journal/urls.py
"""Defines URL patterns for the journal app."""
from django.urls import path

from . import views

app_name = 'journal'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # A page that lists all our prayer topics
    path('topics/', views.topics, name='topics'),
    # Create a page for a specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # A page that lists answered prayers
    path('answered/', views.answered, name='answered'),
]
