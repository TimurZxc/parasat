from django.db import models
import os
from django.conf import settings
import re

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='news_images/', default='default_images/default_news.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_for_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
    def __str__(self):
        return f'Comment by {self.author_email}'

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)


class Video(models.Model):
    title = models.CharField(max_length=500)
    video_id = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='video_previews/', default='default_images/default_video.png')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    video_for_main = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
    def __str__(self):
        return f'{self.title} | {self.video_id} | {self.url}'

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
    