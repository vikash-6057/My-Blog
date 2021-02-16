from django.urls import path,include
from .views import UserSignUp
urlpatterns = [
    path('signup/',UserSignUp.as_view(),name='signup'),
    
]