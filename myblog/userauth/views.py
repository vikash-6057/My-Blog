from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.
class UserSignUp(CreateView):
    form_class=UserCreationForm
    template_name='registration/signup.html'
    # name the file as "registration"
    success_url=reverse_lazy('login')