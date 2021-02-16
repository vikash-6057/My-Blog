from django.urls import path,include
from home.views import HomeView,ArticleView,AddPostView,UpdatePostView,DeletePostView
urlpatterns = [
    # Don't forget to add templates in settings.py
    path('',HomeView.as_view(),name="home"),
    path('article<int:pk>',ArticleView.as_view(),name="article"),
    path('addpost/',AddPostView.as_view(),name="addpost"),
    path('article/edit<int:pk>',UpdatePostView.as_view(),name="edit"),
    path('article<int:pk>/delete',DeletePostView.as_view(),name='delete'),
]