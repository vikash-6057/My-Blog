from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date,datetime
# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publication_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=250)
    likes=models.ManyToManyField(User,related_name='blog_post')

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + " - " + str(self.author)

    def get_absolute_url(self):
        # Redirect to the article page
        # we need to add args to make clear which article we want to redirect

        # return reverse('article',args=str(self.id))

        # if we want to redirect to home there is no need of args
        # since there is no ambiguity
        return reverse("home")

class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("home")
    