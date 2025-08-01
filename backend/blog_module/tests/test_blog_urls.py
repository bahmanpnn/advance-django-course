from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from .. import views



class TestUrl(SimpleTestCase):

    def test_blog_index_url(self):
        url=reverse("blog_module:fbv-index")
        second_url=reverse("blog_module:templateview-index")

        self.assertEquals(resolve(url).func,views.index) #function base views
        self.assertEquals(resolve(second_url).func.view_class,views.TemplateView) # class base views(need view_class for cbv)
    
    def test_blog_post_list_url(self):
        url=reverse("blog_module:post-list")

        self.assertEquals(resolve(url).func.view_class,views.PostListView)
    
    def test_blog_post_detail_url(self):
        url=reverse("blog_module:post-detail",kwargs={"pk":1})

        self.assertEquals(resolve(url).func.view_class,views.PostDetailView)
    