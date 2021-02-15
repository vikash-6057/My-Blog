from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
""" def home_view(request):
    return HttpResponse("Hii...") """

class HomeView(ListView):
    model=Post
    template_name='base.html'
class ArticleView(DetailView):
    model=Post
    template_name='article.html'