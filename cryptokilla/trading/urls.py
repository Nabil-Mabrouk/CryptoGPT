from django.urls import path
from .views import (
    TradingBotListView, TradingBotDetailView, TradingBotCreateView, TradingBotUpdateView, TradingBotDeleteView,
    # Include similar views for Trade, Notification, Opportunity, Backtest, and Log
)


urlpatterns = [
    path('tradingbots/', TradingBotListView.as_view(), name='tradingbot-list'),
    path('tradingbots/<int:pk>/', TradingBotDetailView.as_view(), name='tradingbot-detail'),
    path('tradingbots/create/', TradingBotCreateView.as_view(), name='tradingbot-create'),
    path('tradingbots/<int:pk>/update/', TradingBotUpdateView.as_view(), name='tradingbot-update'),
    path('tradingbots/<int:pk>/delete/', TradingBotDeleteView.as_view(), name='tradingbot-delete'),
    # Include similar URL patterns for Trade, Notification, Opportunity, Backtest, and Log
]
