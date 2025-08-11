import pytest
from datetime import datetime
from rest_framework.test import APIClient,APIRequestFactory
from django.urls import reverse
from blog_module.models import Post


@pytest.mark.django_db # this decorator is neccessary to have access database and for class or methods that need connection with database must we use this decorator.
class TestBlogPostApi:
    client=APIClient()

    def test_get_posts_response_200(self):
        # client=APIRequestFactory() # this is like APIClient but when we doesnt need authentication can use this one,but api client is more common to use because authentication uses for most of endpoints.
        url=reverse("blog_module:api-v1:post-list-api-view")
        response=self.client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self):
        url=reverse("blog_module:api-v2:post-model-viewset")
        data={
            "author":self.user_profile,
            "title":'test title',
            "content":'test content',
            "status":True,
            "category":None,
            "published_date":datetime.now()
        }
        response=self.client.post(url,data)
        assert response.status_code == 401 # status code of response is 401 because user and request need authentication