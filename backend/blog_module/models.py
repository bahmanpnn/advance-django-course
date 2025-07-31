from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Post(models.Model):
    """This is a class to define posts for blog app"""

    # author=models.ForeignKey(User,on_delete=models.CASCADE)
    # author=models.ForeignKey(Profile, on_delete=models.CASCADE)
    author = models.ForeignKey(
        "account_module.Profile", on_delete=models.CASCADE
    )
    image = models.ImageField(
        null=True, blank=True
    )  # need to install pillow package
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )
    status = models.BooleanField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return f"{self.content[:5]}..."

    def get_absolute_api_url(self):
        # router.register('post-model-viewset',v2_views.PostListModelViewSet,basename='post-model-viewset')
        # post-model-viewset-detail ==>
        # base_name + detail or other path that django view set create automaticaly
        # post-model-viewset-detail ==> post-model-viewset + detail
        return reverse(
            "blog_module:api-v2:post-model-viewset-detail",
            kwargs={"pk": self.pk},
        )


class Category(models.Model):
    """This is a class to define categories for posts of blog app"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
