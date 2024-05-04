from django.urls import path
from .views import *


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('news', AllNewsView.as_view(), name='all_news'),
    path('news/<int:pk>', NewsView.as_view(), name='news'),
    path('about-us', AboutUsView.as_view(), name='about_us'),
]