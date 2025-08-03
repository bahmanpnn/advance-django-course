from django.test import TestCase,Client
from django.urls import reverse


class TestBlogView(TestCase):
    def setUp(self):
        self.client=Client()
    
    def test_blog_index_url_successfull_response(self):
        url=reverse('blog_module:fbv-index')
        response=self.client.get(url)
        
        self.assertEquals(response.status_code,200)
        self.assertTrue(str(response.content).find('index'))
        self.assertTemplateUsed(response,template_name="index.html")
        self.assertTemplateNotUsed(response,template_name="index2.html")