from django.urls import path
from .views import IndexView
from .views import ConfigCreateView, ConfigUpdateView, ConfigDeleteView, config_list

urlpatterns = [
    path('', IndexView.as_view(), name='landing-home'),
    path('config/', config_list.as_view(), name='config-list'),
    path('config/create/', ConfigCreateView.as_view(), name='config-create'),
    path('config/<int:pk>/update/', ConfigUpdateView.as_view(), name='config-update'),
    path('config/<int:pk>/delete/', ConfigDeleteView.as_view(), name='config-delete'),
]
