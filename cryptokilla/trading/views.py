from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import TradingBot, Trade, Notification, Opportunity, Backtest, Log
from .forms import TradingBotForm, TradeForm, NotificationForm, OpportunityForm, BacktestForm, LogForm

# Decorator to require login for views
@method_decorator(login_required, name='dispatch')
class TradingBotListView(ListView):
    model = TradingBot
    template_name = 'trading/tradingbot_list.html'
    context_object_name = 'tradingbots'

@method_decorator(login_required, name='dispatch')
class TradingBotDetailView(DetailView):
    model = TradingBot
    template_name = 'trading/tradingbot_detail.html'
    context_object_name = 'tradingbot'

@method_decorator(login_required, name='dispatch')
class TradingBotCreateView(CreateView):
    model = TradingBot
    form_class = TradingBotForm
    template_name = 'trading/tradingbot_form.html'
    success_url = reverse_lazy('trading:tradingbot-list')

@method_decorator(login_required, name='dispatch')
class TradingBotUpdateView(UpdateView):
    model = TradingBot
    form_class = TradingBotForm
    template_name = 'trading/tradingbot_form.html'
    context_object_name = 'tradingbot'
    success_url = reverse_lazy('trading:tradingbot-list')

@method_decorator(login_required, name='dispatch')
class TradingBotDeleteView(DeleteView):
    model = TradingBot
    template_name = 'trading/tradingbot_confirm_delete.html'
    context_object_name = 'tradingbot'
    success_url = reverse_lazy('trading:tradingbot-list')

# Repeat similar views for Trade, Notification, Opportunity, Backtest, and Log
