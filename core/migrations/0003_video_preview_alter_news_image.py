# Generated by Django 5.0.4 on 2024-04-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_video_news_news_for_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preview',
            field=models.ImageField(blank=True, default='default_images/default_video.png', null=True, upload_to='video_previews/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='default_images/default_news.png', null=True, upload_to='news_images/'),
        ),
    ]
