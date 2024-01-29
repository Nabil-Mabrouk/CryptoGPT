from django.db import models

class Config(models.Model):
    main_font = models.CharField(max_length=50, default='Poppins')
    default_text_color = models.CharField(max_length=20, default='rgb(255, 255, 255)')
    background_image_url = models.CharField(max_length=100, default='url("header-backgroud.jpg")')
    background_color_default = models.CharField(max_length=20, default='rgb(0, 0, 0, 0.7)')
    navbar_background_color = models.CharField(max_length=20, default='transparent')
    navbar_scrolled_background_color = models.CharField(max_length=20, default='rgba(0, 0, 0, 0.5)')
    navbar_scrolled_background_blur = models.IntegerField(default=10)
    btn_navbar_background_color = models.CharField(max_length=20, default='#000000')

    home_image_prosition_choices = [
        ('left', 'Left'),
        ('right', 'Right'),
        ('center', 'Center'),
        ('none', 'None'),
    ]
    home_image_prosition = models.CharField(max_length=10, choices=home_image_prosition_choices, default='left')
    home_image_url = models.URLField(default='https://placehold.co/600x400')
    home_text_title = models.CharField(max_length=255, default='CryptoKilla')
    home_text_subtitle = models.CharField(max_length=255, default='Everything you need to crack the market')
    home_text_paragraph = models.TextField(default='Market, news, trade, analyse, bots and much more ..')

    features_background_color = models.CharField(max_length=20, default='')

    sections_features_list = models.JSONField(default=[
        {"image_url": "default_image_url1", "body_text": "Default body text 1"},
        {"image_url": "default_image_url2", "body_text": "Default body text 2"},
        # Add more default values as needed
    ])

    index_background_color = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"Configuration - {self.id}"
