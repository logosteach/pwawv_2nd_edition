# project_2/journal/views.py
from django.shortcuts import render
from .models import Topic, Entry


def index(request):
    """The home page for the journal app."""
    context = {
        'topic_count': Topic.objects.count(),
        'entry_count': Entry.objects.count(),
    }
    return render(request, 'journal/index.html', context)


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
