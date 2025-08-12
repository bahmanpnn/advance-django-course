from django.test import TestCase
from datetime import datetime

from ..models import Post, Category
from django.contrib.auth import get_user_model
from account_module.models import User, Profile


class TestPostModel(TestCase):
    """
    author model has relation with profile not user directly, but we used signals to create profile model after user creation;
    so we dont need to create new profile for that user again and django handle it in test and test database.
    """

    def test_create_post_with_valid_data(self):

        # first way to get new user with django authentication user model that find auto default user that set in project
        default_user = get_user_model()
        first_new_user = default_user.objects.create_user(
            email="test@test.com", password="Ab12345!@"
        )

        # second way to create user with importin user directly from its model and app
        second_new_user = User.objects.create_user(
            email="test2@test.com", password="Ab12345!@"
        )

        # third way that works for both we can create new object from user model and then save it in database==>new_user.save()
        third_new_user = User(email="test3@test.com", password="Ab12345!@")
        third_new_user.save()

        check_first_user = User.objects.filter(
            email=first_new_user.email
        ).exists()
        check_second_user = User.objects.get(email=second_new_user.email)
        check_third_user = User.objects.get(email=third_new_user.email)

        # print(check_first_user)
        # print(check_second_user)
        # print(check_third_user)

        post = Post.objects.create(
            author=Profile.objects.get(user=check_third_user),
            title="test title",
            content="test content",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertEqual(post.title, "test title")


class TestSecondPostModel(TestCase):
    """
    remember that author model has relation with profile not user directly, but we used signals to create profile model after user creation;
     so we dont need to create new profile for that user again and django handle it in test and test database.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email="test2@test.com", password="Ab12345!@"
        )
        self.user_profile = Profile.objects.get(
            user=User.objects.get(email=self.user.email)
        )
        return super().setUp()

    def test_create_post_with_valid_data(self):

        post = Post.objects.create(
            author=self.user_profile,
            title="test title",
            content="test content",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, "test title")
