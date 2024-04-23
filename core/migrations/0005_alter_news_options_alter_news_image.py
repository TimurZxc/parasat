# Generated by Django 4.2.7 on 2024-04-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_news_image_alter_video_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='default_images/default_news.png', null=True, upload_to='news_images/'),
        ),
    ]
