from django.shortcuts import render, redirect
from django.views import generic, View
from .models import *   

class MainView(generic.ListView):
    template_name = 'main.html'
    model = News
    context_object_name = 'news_list'

    def get_news_queryset(self):
        queryset = News.objects.filter(news_for_main=True)
        return queryset
    
    def get_video_queryset(self):
        queryset = Video.objects.filter(video_for_main=True)
        return queryset
    
    def get(self, request):
        return render(request, self.template_name, {'news_list': self.get_news_queryset(), 'video_list': self.get_video_queryset()})
