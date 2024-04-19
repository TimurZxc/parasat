# Generated by Django 5.0.4 on 2024-04-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_video_preview_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default='default_images/default_news.png', upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='preview',
            field=models.ImageField(default='default_images/default_video.png', upload_to='video_previews/'),
        ),
    ]
