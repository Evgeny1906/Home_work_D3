from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Author
from datetime import datetime
from pprint import pprint
# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'newses.html'
    context_object_name = 'newses'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()

        return context




class NewsDeta(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'