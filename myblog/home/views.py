from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post,Category
from .forms import AddPostForm
from django.urls import reverse_lazy,reverse

# Create your views here.
""" def home_view(request):
    return HttpResponse("Hii...") """


class HomeView(ListView):
    model = Post
    template_name = "base.html"
    ordering=['-publication_date']

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context["category"] =Category.objects.all() 
        return context
    


class ArticleView(DetailView):
    model = Post
    template_name = "article.html"

    def get_context_data(self, *args, **kwargs):
        context=super().get_context_data(*args, **kwargs)
        likes_obj = get_object_or_404(Post,id=self.kwargs['pk'])
        liked =False
        if likes_obj.likes.filter(id=self.request.user.id).exists():
            liked = True
        number_of_likes = likes_obj.total_likes()
        context['total_likes']=number_of_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    form_class = AddPostForm
    # fields='__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields = ["title", "category" , "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")

class AddCategoryView(CreateView):
    model = Category
    template_name='category_add.html'
    fields = '__all__'
    
class CategoryView(ListView):
    template_name='category_view.html'
    def get(self,request,name):
        category_list=Post.objects.filter(category=name)
        return render(request,self.template_name,{'name':name,'category_list':category_list})

# same can be implemented as functional based view
""" def CategoryView(request,name):
    category_list=Post.objects.filter(category=name)
    return render(request,'category_view.html',{'name':name,'category_list':category_list}) """

class AuthorView(ListView):
    template_name='author_view.html'
    def get(self,request):
        author_list=Post.objects.filter(author=self.request.user)
        return render(request,self.template_name,{'author_list':author_list})

def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))