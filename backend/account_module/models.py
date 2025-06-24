from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
# from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """
        Custom user model manager where email is the unique identifiers authentication instead of usernames.
    """
    def create_user(self,email,password,**extra_fields):
        ''' create and save a simple user with the given email and password with extra data'''
        if not email:
            # raise ValueError(_("the Email must be set"))
            raise ValueError("the Email must be set")
        email= self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self,email,password,**extra_fields):
        ''' create and save a super user with the given email and password with extra data'''
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') is not True:
            # raise ValueError(_("superuser must have is_staff=True."))
            raise ValueError("superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            # raise ValueError(_("superuser must have is_superuser=True."))
            raise ValueError("superuser must have is_superuser=True.")
        return self.create_user(email,password,**extra_fields)


class User(AbstractBaseUser,PermissionsMixin):
    """
        Custom user model for the project
    """

    email=models.EmailField(max_length=255,unique=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    # is_verified=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    # REQUIRED_FIELDS=['phone_number']

    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    objects=UserManager()
    def __str__(self):
        return self.email


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=32,unique=True,null=True,blank=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    # avatar=models.ImageField(null=True,blank=True)
    description=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
