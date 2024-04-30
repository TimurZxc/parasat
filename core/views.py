from django.shortcuts import render, redirect
from django.views import generic, View
from .models import * 
from .forms import *  
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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
    

class AllNewsView(generic.ListView):
    template_name = 'all_news.html'
    model = News
    context_object_name = 'all_news_list'
    paginate_by = 4

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')
        return queryset
    

class NewsView(generic.DetailView):
    template_name = 'news.html'
    model = News
    context_object_name = 'news'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        context['comment_form'] = CommentForm()
        return context
    
    def get_success_url(self):
        return reverse('news', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = self.object
            new_comment.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = self.get_context_data()
            context['comment_form'] = comment_form
            return self.render_to_response(context)

    


