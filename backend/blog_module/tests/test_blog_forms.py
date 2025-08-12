from django.test import TestCase, SimpleTestCase
from datetime import datetime
from ..models import Category
from ..forms import PostForm, PostCreateForm
from account_module.models import (
    User,
    Profile,
)  # or import get user model from django contrib


class TestPostCreateForm(TestCase):
    def test_post_form_with_valid_data(self):
        category_obj = Category.objects.create(name="test_category")
        form = PostCreateForm(
            data={
                "title": "test post title",
                "content": "this is a test post content",
                "status": True,
                "category": category_obj,
                "published_date": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):

        form = PostCreateForm(data={})
        self.assertFalse(form.is_valid())


class TestPostForm(TestCase):
    """for creating a test author for all methods we can use dispatch method but here i create and handle author like category"""

    def test_post_form_with_valid_data(self):
        new_user = User.objects.create_user("test@test.com", "Ab1234!@")

        user_profile = Profile.objects.get(user=new_user)

        category_obj = Category.objects.create(name="test_category")
        form = PostCreateForm(
            data={
                "author": user_profile,
                "title": "test post title",
                "content": "this is a test post content",
                "status": True,
                "category": category_obj,
                "published_date": datetime.now(),
            }
        )
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):

        form = PostCreateForm(data={})
        self.assertFalse(form.is_valid())
