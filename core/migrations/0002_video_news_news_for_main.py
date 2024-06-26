# Generated by Django 5.0.4 on 2024-04-19 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('video_id', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('video_for_main', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_for_main',
            field=models.BooleanField(default=False),
        ),
    ]
