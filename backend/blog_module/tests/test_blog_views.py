from datetime import datetime
from django.test import TestCase,Client
from django.urls import reverse
from ..models import Post,Category
from account_module.models import User,Profile


class TestBlogView(TestCase):
    def setUp(self):
        self.client=Client()

        self.user=User.objects.create_user(email="test2@test.com",password="Ab12345!@")
        self.user_profile=Profile.objects.get(user=User.objects.get(email=self.user.email))
        self.post=Post.objects.create(
            author=self.user_profile,
            title='test title',
            content='test content',
            status=True,
            category=None,
            published_date=datetime.now()
        )
    
    def test_blog_index_url_successfull_response(self):
        url=reverse('blog_module:fbv-index')
        response=self.client.get(url)
        
        self.assertEquals(response.status_code,200)
        self.assertTrue(str(response.content).find('index'))
        self.assertTemplateUsed(response,template_name="index.html")
        self.assertTemplateNotUsed(response,template_name="index2.html")
    

    def test_blog_post_detail_anonymouse_response(self):
        url=reverse("blog_module:post-detail",kwargs={"pk":self.post.id})
        response=self.client.get(url)
        self.assertEquals(response.status_code,302) # because of login required mixin anonymouse user redirect to login page and status code is 302.
        
    def test_blog_post_detail_logged_in_user_response(self):
        self.client.force_login(self.user) # force login method uses to login user in client and tests.
        url=reverse("blog_module:post-detail",kwargs={"pk":self.post.id})
        response=self.client.get(url)
        self.assertEquals(response.status_code,200) # because of login required mixin anonymouse user redirect to login page and status code is 302.
