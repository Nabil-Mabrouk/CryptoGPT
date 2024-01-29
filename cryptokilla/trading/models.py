# trading/models.py
from django.db import models
from users.models import CustomUser
from market.models import TradingPair

class TradeActionEnum(models.TextChoices):
    BUY = 'buy', 'Buy'
    SELL = 'sell', 'Sell'

class TradeStatusEnum(models.TextChoices):
    OPEN = 'open', 'Open'
    CLOSED = 'closed', 'Closed'

class NotificationTypeEnum(models.TextChoices):
    EMAIL = 'email', 'Email'
    SMS = 'sms', 'Sms'




class Strategy(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def execute_strategy(self, trading_bot, opportunity):
        raise NotImplementedError("Subclasses must implement this method")

class TrendFollowingStrategy(Strategy):
    # You can add specific fields for the Trend Following strategy here
    pass

class TradingBot(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    bot_name = models.CharField(max_length=255)
    allocated_capital = models.FloatField()
    current_capital = models.FloatField()
    risk_percentage = models.FloatField()  # Percentage of capital to risk per trade
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Trade(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trading_bot = models.ForeignKey(TradingBot, on_delete=models.CASCADE)
    trading_pair = models.ForeignKey(TradingPair, on_delete=models.CASCADE)
    action = models.CharField(max_length=4, choices=TradeActionEnum.choices)
    quantity = models.FloatField()
    price = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=TradeStatusEnum.choices)

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=10, choices=TradeStatusEnum.choices)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Opportunity(models.Model):
    trading_pair = models.CharField(max_length=10)
    time_frame = models.CharField(max_length=10)
    strategy_type = models.CharField(max_length=50)
    status = models.CharField(max_length=10)  # open or closed
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Backtest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    trading_pair = models.CharField(max_length=10)
    strategy_parameters = models.TextField()
    performance_metrics = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Log(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    log_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

