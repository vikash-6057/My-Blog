from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
# Create your views here.
class UserSignUp(CreateView):
    form_class= SignUpForm
    template_name='registration/signup.html'
    # name the file as "registration"
    success_url=reverse_lazy('login')