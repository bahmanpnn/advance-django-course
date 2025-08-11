import pytest
from datetime import datetime
from rest_framework.test import APIClient,APIRequestFactory
from django.urls import reverse
from blog_module.models import Post,Category
from account_module.models import User,Profile



@pytest.fixture
def api_client():
    client=APIClient()
    return client

@pytest.fixture
def common_user():
    user=User.objects.create_user(email="test@test.com",password="Ab12345!@",is_verified=True)
    return user


@pytest.mark.django_db # this decorator is neccessary to have access database and for class or methods that need connection with database must we use this decorator.
class TestBlogPostApi:
    client=APIClient()

    # def setUp(self):
    #     self.user=User.objects.create_user(email="test2@test.com",password="Ab12345!@")
    #     self.user_profile=Profile.objects.get(user=User.objects.get(email=self.user.email))
    #     self.category_obj=Category.objects.create(name='test_category')
    #     return super().setUp()

    def test_get_posts_response_200(self,api_client):
        # client=APIRequestFactory() # this is like APIClient but when we doesnt need authentication can use this one,but api client is more common to use because authentication uses for most of endpoints.
        url=reverse("blog_module:api-v1:post-list-api-view")
        # response=self.client.get(url)
        response=api_client.get(url)
        assert response.status_code == 200
    
    def test_create_post_response_401_status(self,api_client):

        url=reverse("blog_module:api-v2:post-model-viewset-list") # post-model-viewset + list ==> post-model-viewset-list
        data={
            # "author":self.user_profile,
            "title":'test title',
            "content":'test content',
            "status":True,
            # "category":self.category_obj,
            "published_date":datetime.now()
        }
        response=api_client.post(url,data)
        assert response.status_code == 401 # status code of response is 401 because user and request need authentication

    def test_create_post_response_201_status(self,api_client,common_user):

        url=reverse("blog_module:api-v2:post-model-viewset-list")
        data={
            "title":'test title',
            "content":'test content',
            "status":True,
            "published_date":datetime.now()
        }
        user=common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response=api_client.post(url,data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self,api_client,common_user):

        url=reverse("blog_module:api-v2:post-model-viewset-list")
        data={
            "title":'test title',
            "content":'test content',
        }
        user=common_user
        # api_client.force_login(user=user)
        api_client.force_authenticate(user=user)
        response=api_client.post(url,data)
        assert response.status_code == 400


    # add another tests for delete,update or another actions with pytest


