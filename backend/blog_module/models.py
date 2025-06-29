from django.db import models
from account_module.models import Profile
# from django.contrib.auth import get_user_model

# User=get_user_model()

class Post(models.Model):
    ''' This is a class to define posts for blog app'''
    # author=models.ForeignKey('Profile',on_delete=models.CASCADE) 
    # for avoiding to spagheti form of looping we must import directly model.so we import in in field of model directly.
    author=models.ForeignKey('account_module.Profile',on_delete=models.CASCADE,null=True)
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



