from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Cryptocurrency, TradingPair, CryptocurrencyNews
from channels.layers import get_channel_layer
from asgiref.testing import ApplicationCommunicator



class CryptocurrencyListView(ListView):
    model = Cryptocurrency
    template_name = 'market/cryptocurrency_list.html'  # Create a template for displaying the list
    context_object_name = 'cryptocurrencies'
    paginate_by = 10  # Adjust the number of cryptocurrencies per page if needed

class CryptocurrencyDetailView(DetailView):
    model = Cryptocurrency
    template_name = 'market/cryptocurrency_detail.html'  # Create a template for displaying the details

class TradingPairListView(ListView):
    model = TradingPair
    template_name = 'market/trading_pair_list.html'  # Create a template for displaying the list
    context_object_name = 'trading_pairs'
    paginate_by = 10  # Adjust the number of trading pairs per page if needed

class CryptocurrencyNewsListView(ListView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_list.html'  # Create a template for displaying the list
    context_object_name = 'cryptocurrency_news'
    paginate_by = 10  # Adjust the number of news articles per page if needed
    ordering = ['-timestamp']  # Show the latest news first

class CryptocurrencyNewsDetailView(DetailView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_detail.html'  # Create a template for displaying the details


class CryptocurrencyCreateView(CreateView):
    model = Cryptocurrency
    template_name = 'market/cryptocurrency_form.html'  # Create a template for the form
    success_url = reverse_lazy('cryptocurrency-list') 
    fields = ['name', 'symbol', 'description', 'website', 'icon', 'is_stablecoin']

class CryptocurrencyUpdateView(UpdateView):
    model = Cryptocurrency
    template_name = 'market/cryptocurrency_form.html'  # Create a template for the form
    fields = ['name', 'symbol', 'description', 'website', 'icon', 'is_stablecoin']

class CryptocurrencyDeleteView(DeleteView):
    model = Cryptocurrency
    template_name = 'market/cryptocurrency_confirm_delete.html'  # Create a template for confirmation
    success_url = reverse_lazy('cryptocurrency-list')  # Redirect to the cryptocurrency list view after deletion

# Repeat similar views for TradingPair and CryptocurrencyNews
class TradingPairDetailView(DetailView):
    model = TradingPair
    template_name = 'market/trading_detail.html'  # Create a template for displaying the details

class TradingPairCreateView(CreateView):
    model = TradingPair
    template_name = 'market/trading_pair_form.html'  # Create a template for the form
    fields = ['base_currency', 'quote_currency']

class TradingPairUpdateView(UpdateView):
    model = TradingPair
    template_name = 'market/trading_pair_form.html'  # Create a template for the form
    fields = ['base_currency', 'quote_currency']

class TradingPairDeleteView(DeleteView):
    model = TradingPair
    template_name = 'market/trading_pair_confirm_delete.html'  # Create a template for confirmation
    success_url = reverse_lazy('tradingpair-list')  # Redirect to the trading pair list view after deletion

class CryptocurrencyNewsDetailView(DetailView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_detail.html'  # Create a template for displaying the details

class CryptocurrencyNewsCreateView(CreateView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_form.html'  # Create a template for the form
    fields = ['cryptocurrency', 'title', 'content', 'source']
    success_url = reverse_lazy('cryptocurrencynews-list')
    
class CryptocurrencyNewsUpdateView(UpdateView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_form.html'  # Create a template for the form
    fields = ['cryptocurrency', 'title', 'content', 'source']

class CryptocurrencyNewsDeleteView(DeleteView):
    model = CryptocurrencyNews
    template_name = 'market/cryptocurrency_news_confirm_delete.html'  # Create a template for confirmation
    success_url = reverse_lazy('cryptocurrencynews-list')  # Redirect to the news list view after deletion

async def trigger_news_update(news_message):
    channel_layer = get_channel_layer()
    await channel_layer.group_send('news_group', {'type': 'send.news.update', 'message': news_message})

def add_cryptocurrency_news(request):
    # Your logic to add a new CryptocurrencyNews instance
    new_news = CryptocurrencyNews.objects.create(
        cryptocurrency=some_cryptocurrency_instance,
        title="New News Title",
        content="News content goes here.",
        source="https://example.com",
    )

    # Trigger WebSocket event to broadcast news update
    trigger_news_update(new_news.title)
    return HttpResponse("News added successfully")
