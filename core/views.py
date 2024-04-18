from django.shortcuts import render, redirect
from django.views import generic, View
from .models import *   

class MainView(generic.ListView):
    template_name = 'main.html'
    model = News
    context_object_name = 'news_list'

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')[:3]
        return queryset

    def get(self, request):
        return render(request, self.template_name, {'news_list': self.get_queryset()})
