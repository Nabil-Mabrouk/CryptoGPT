from django.shortcuts import render
from user_visit.models import UserVisit
from django.views.generic import ListView


class UserVisitListView(ListView):
    model = UserVisit
    template_name = 'stats/stats.html'  # Create a template for displaying the list
    context_object_name = 'visits'
    paginate_by = 10  # Adjust the number of news articles per page if needed
    ordering = ['-timestamp']  # Show the latest news first
