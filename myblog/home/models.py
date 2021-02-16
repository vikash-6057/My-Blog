from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title+ ' - '+ str(self.author)

    def get_absolute_url(self):
        # Redirect to the article page 
        # we need to add args to make clear which article we want to redirect

        #return reverse('article',args=str(self.id))
        # if we want to redirect to home there is no need of args 
        # since there is no ambiguity
        return reverse('home')