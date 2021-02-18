from django import forms
from .models import Post,Category

choices=Category.objects.values_list('name','name')
choice_list=[]
for choice in choices:
    choice_list.append(choice)
""" class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__" """

class AddPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','author','category','body')
        widgets = {
            'title':forms.TextInput(),
            'author':forms.TextInput(attrs={'id':'curuser','value':'','type':'hidden'}),
            'category':forms.Select(choices=choice_list),
            'body' : forms.Textarea(),

        }
