from django.urls import path
from .views import (
    CryptocurrencyListView, CryptocurrencyDetailView,
    CryptocurrencyCreateView, CryptocurrencyUpdateView, CryptocurrencyDeleteView,
    TradingPairListView, TradingPairDetailView, TradingPairCreateView, TradingPairUpdateView, TradingPairDeleteView,
    CryptocurrencyNewsDetailView,
    CryptocurrencyNewsListView, CryptocurrencyNewsCreateView, CryptocurrencyNewsUpdateView, CryptocurrencyNewsDeleteView
)


urlpatterns = [
    # Cryptocurrency URLs
    path('cryptocurrencies/', CryptocurrencyListView.as_view(), name='cryptocurrency-list'),
    path('cryptocurrencies/<int:pk>/', CryptocurrencyDetailView.as_view(), name='cryptocurrency-detail'),
    path('cryptocurrencies/create/', CryptocurrencyCreateView.as_view(), name='cryptocurrency-create'),
    path('cryptocurrencies/<int:pk>/update/', CryptocurrencyUpdateView.as_view(), name='cryptocurrency-update'),
    path('cryptocurrencies/<int:pk>/delete/', CryptocurrencyDeleteView.as_view(), name='cryptocurrency-delete'),

    # TradingPair URLs
    path('tradingpairs/', TradingPairListView.as_view(), name='tradingpair-list'),
    path('tradingpairs/<int:pk>/', TradingPairDetailView.as_view(), name='tradingpair-detail'),
    path('tradingpairs/create/', TradingPairCreateView.as_view(), name='tradingpair-create'),
    path('tradingpairs/<int:pk>/update/', TradingPairUpdateView.as_view(), name='tradingpair-update'),
    path('tradingpairs/<int:pk>/delete/', TradingPairDeleteView.as_view(), name='tradingpair-delete'),

    # CryptocurrencyNews URLs
    path('cryptocurrencynews/', CryptocurrencyNewsListView.as_view(), name='cryptocurrencynews-list'),
    path('cryptocurrencynews/<int:pk>/', CryptocurrencyNewsDetailView.as_view(), name='cryptocurrencynews-detail'),
    path('cryptocurrencynews/create/', CryptocurrencyNewsCreateView.as_view(), name='cryptocurrencynews-create'),
    path('cryptocurrencynews/<int:pk>/update/', CryptocurrencyNewsUpdateView.as_view(), name='cryptocurrencynews-update'),
    path('cryptocurrencynews/<int:pk>/delete/', CryptocurrencyNewsDeleteView.as_view(), name='cryptocurrencynews-delete'),
]
