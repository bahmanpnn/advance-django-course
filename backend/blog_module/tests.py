from django.test import TestCase,SimpleTestCase
from django.urls import reverse,resolve
from . import views



class TestUrl(SimpleTestCase):
    def test_blog_index_url(self):
        url=reverse("blog_module:fbv-index")
        second_url=reverse("blog_module:templateview-index")
        # third_url=reverse("blog_module:cbv-templateview-index") # need argument passing handling

        self.assertEquals(resolve(url).func,views.index)
        self.assertEquals(resolve(second_url).func.view_class,views.TemplateView)
        # self.assertEquals(resolve(third_url).func.view_class,views.IndexTemplateView)