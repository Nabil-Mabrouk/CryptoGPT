from django.db import models
from django.utils import timezone

# Create your models here.
class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    icon = models.ImageField(upload_to='cryptocurrency_icons/', blank=True, null=True)
    is_stablecoin = models.BooleanField(default=False)  # Add this field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class TradingPair(models.Model):
    base_currency = models.ForeignKey(Cryptocurrency, related_name='base_currency', on_delete=models.CASCADE)
    quote_currency = models.ForeignKey(Cryptocurrency, related_name='quote_currency', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.base_currency.symbol}/{self.quote_currency.symbol}"

class CryptocurrencyNews(models.Model):
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    source = models.URLField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cryptocurrency.name} News: {self.title}"