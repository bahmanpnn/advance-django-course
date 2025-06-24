from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class Post(models.Model):
    ''' This is a class to define posts for blog app'''
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # image=models.ImageField(null=True,blank=True) # need to install pillow package
    title=models.CharField(max_length=255)
    content=models.TextField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    status=models.BooleanField()
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    published_date=models.DateTimeField()

    def __str__(self):
        return self.title


class Category(models.Model):
    ''' This is a class to define categories for posts of blog app'''
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name



