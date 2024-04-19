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
    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_news = News.objects.get(pk=self.pk)
                if old_news.image and (not self.image or old_news.image != self.image) and old_news.image.name != 'default_images/default_news.png':
                    old_image_path = os.path.join(settings.MEDIA_ROOT, old_news.image.name)
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)
            except News.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    def delete(self, *args, **kwargs):
        if self.image and self.image.name != 'default_images/default_news.png':
            image_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            if os.path.isfile(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    def __str__(self):
        return f'{self.title} | {self.video_id} | {self.url}'

    def save(self, *args, **kwargs):
        if self.pk:
            try:
                old_video = Video.objects.get(pk=self.pk)
                if old_video.preview and (not self.preview or old_video.preview != self.preview) and old_video.preview.name != 'default_images/default_video.png':
                    old_image_path = os.path.join(settings.MEDIA_ROOT, old_video.preview.name)
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)
            except Video.DoesNotExist:
                pass
        if self.url:
            match = re.search(r'\?v=([^&]+)', self.url)
            if match:
                self.video_id = match.group(1)
        super().save(*args, **kwargs)

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
        
    def delete(self, *args, **kwargs):
        if self.preview and self.preview.name != 'default_images/default_video.png':
            image_path = os.path.join(settings.MEDIA_ROOT, self.preview.name)
            if os.path.isfile(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)

    