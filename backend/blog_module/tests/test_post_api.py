import pytest
from rest_framework.test import APIClient,APIRequestFactory
from django.urls import reverse


@pytest.mark.django_db # this decorator is neccessary to have access database and for class or methods that need connection with database must we use this decorator.
class TestBlogPostApi:
    def test_get_posts_response_200(self):
        # client=APIRequestFactory() # this is like APIClient but when we doesnt need authentication can use this one,but api client is more common to use because authentication uses for most of endpoints.
        client=APIClient()
        url=reverse("blog_module:api-v1:post-list-api-view")
        response=client.get(url)
        assert response.status_code == 200