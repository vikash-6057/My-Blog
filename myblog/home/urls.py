from django.urls import path,include
from home.views import HomeView,ArticleView,AddPostView
urlpatterns = [
    # Don't forget to add templates in settings.py
    path('',HomeView.as_view(),name="home"),
    path('article<int:pk>',ArticleView.as_view(),name="article"),
    path('addpost',AddPostView.as_view(),name="addpost"),
]