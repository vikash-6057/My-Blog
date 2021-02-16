from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import AddPostForm
from django.urls import reverse_lazy

# Create your views here.
""" def home_view(request):
    return HttpResponse("Hii...") """


class HomeView(ListView):
    model = Post
    template_name = "base.html"
    ordering=['-publication_date']


class ArticleView(DetailView):
    model = Post
    template_name = "article.html"


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = AddPostForm
    # fields='__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
