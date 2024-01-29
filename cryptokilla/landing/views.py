# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Config
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Config
from .forms import ConfigForm  # Create a forms.py file to define the ConfigForm

class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['config'] = Config.objects.first()  # Assuming you have only one configuration object
        return context

class ConfigCreateView(CreateView):
    model = Config
    form_class = ConfigForm
    template_name = 'landing/config_form.html'  # Create a template for the form
    success_url = '/landing/'  # Redirect to the config list view after creation

class ConfigUpdateView(UpdateView):
    model = Config
    form_class = ConfigForm
    template_name = 'landing/config_form.html'  # Create a template for the form
    success_url = '/'  # Redirect to the config list view after update

class ConfigDeleteView(DeleteView):
    model = Config
    template_name = 'landing/config_confirm_delete.html'  # Create a template for confirmation
    success_url = '/landing/'  # Redirect to the config list view after deletion

class config_list(ListView):
    model = Config
    template_name = 'landing/config_list.html'
    context_object_name = 'configs'
