from django.shortcuts import render
from django.views.generic import ListView
from easyaudit.models import RequestEvent


class UserVisitListView(ListView):
    model = RequestEvent
    template_name = 'stats/stats.html'  # Create a template for displaying the list
    context_object_name = 'visits'
    paginate_by = 10  # Adjust the number of news articles per page if needed
    ordering = ['-datetime']  # Show the latest news first
