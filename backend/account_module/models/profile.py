from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .user import User

# from django.contrib.auth import get_user_model

# User=get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=32, unique=True, null=True, blank=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.ImageField(null=True, blank=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f'{self.user.email}'
        return self.user.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    this function is a signal and create a profile after creating a new user object with post_save.
    sender is a model or class that is a trigger action.
    instance is an object of sender model/class.
    created is a bool type and if instnace created value is true it means that it created and function uses for first time.
    if we update instance of sender model/class profile created value is false and we check and use condition to ignore creating new profile instance for user model.
    """
    if created:
        Profile.objects.create(user=instance)
