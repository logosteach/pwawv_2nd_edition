# project_2/journal/views.py
from django.shortcuts import render
from .models import Topic, Entry


def index(request):
    """The home page for the journal app."""
    return render(request, 'journal/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'journal/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'journal/topic.html', context)


def answered(request):
    """Show answered prayers."""
    entries = Entry.objects.filter(status='ANS').order_by('-date_added')
    context = {'entries': entries}
    return render(request, 'journal/answered.html', context)
