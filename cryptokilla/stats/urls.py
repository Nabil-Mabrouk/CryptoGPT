# statistics/urls.py
from django.urls import path
from .views import UserVisitListView

urlpatterns = [
    path('stats/', UserVisitListView.as_view(), name='stats'),
    # Add more URLs as needed
]