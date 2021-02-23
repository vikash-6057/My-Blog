from django.urls import path,include
from home.views import HomeView,ArticleView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView
from home.views import AuthorView,LikeView
urlpatterns = [
    # Don't forget to add templates in settings.py
    path('',HomeView.as_view(),name="home"),
    path('article<int:pk>',ArticleView.as_view(),name="article"),
    path('addpost/',AddPostView.as_view(),name="addpost"),
    path('article/edit<int:pk>',UpdatePostView.as_view(),name="edit"),
    path('article<int:pk>/delete',DeletePostView.as_view(),name='delete'),
    path('add-category/',AddCategoryView.as_view(),name='addcategory'),
    #path('category<str:name>/',CategoryView,name='category'), (?P<int:pk>[^/]+)/$
    path('category/<str:name>/',CategoryView.as_view(),name='category'),
    path('author/',AuthorView.as_view(),name='author'),
    path('like/<int:pk>',LikeView,name="like_post"),
]