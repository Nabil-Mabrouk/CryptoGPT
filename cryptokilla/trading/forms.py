from django import forms
from .models import TradingBot, Trade, Notification, Opportunity, Backtest, Log

class TradingBotForm(forms.ModelForm):
    class Meta:
        model = TradingBot
        fields = '__all__'

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = '__all__'

class BacktestForm(forms.ModelForm):
    class Meta:
        model = Backtest
        fields = '__all__'

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'
