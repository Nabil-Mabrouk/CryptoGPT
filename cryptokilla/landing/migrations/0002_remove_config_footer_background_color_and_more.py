# Generated by Django 5.0.1 on 2024-01-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='footer_background_color',
        ),
        migrations.AddField(
            model_name='config',
            name='background_color_default',
            field=models.CharField(default='rgb(0, 0, 0, 0.7)', max_length=20),
        ),
        migrations.AddField(
            model_name='config',
            name='background_image_url',
            field=models.URLField(default='url("header-backgroud.jpg")'),
        ),
        migrations.AddField(
            model_name='config',
            name='btn_navbar_background_color',
            field=models.CharField(default='#000000', max_length=20),
        ),
        migrations.AddField(
            model_name='config',
            name='default_text_color',
            field=models.CharField(default='rgb(255, 255, 255)', max_length=20),
        ),
        migrations.AddField(
            model_name='config',
            name='features_background_color',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='config',
            name='home_image_prosition',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'Right'), ('center', 'Center')], default='left', max_length=10),
        ),
        migrations.AddField(
            model_name='config',
            name='home_image_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='config',
            name='home_text_paragraph',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='config',
            name='home_text_subtitle',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='config',
            name='home_text_title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='config',
            name='main_font',
            field=models.CharField(default='Poppins', max_length=50),
        ),
        migrations.AddField(
            model_name='config',
            name='navbar_scrolled_background_blur',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='config',
            name='navbar_scrolled_background_color',
            field=models.CharField(default='rgba(0, 0, 0, 0.5)', max_length=20),
        ),
        migrations.AddField(
            model_name='config',
            name='sections_features_list',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='config',
            name='index_background_color',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='config',
            name='navbar_background_color',
            field=models.CharField(default='transparent', max_length=20),
        ),
    ]
