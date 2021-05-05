from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@email.com', password='top_secret')
        self.user2 = User.objects.create_user(username='sergey', email='sergey@email.com', password='top_secret')
        self.user3 = User.objects.create_user(username='andrey', email='andrey@email.com', password='top_secret')
        self.user4 = User.objects.create_user(username='mikhail', email='mikhail@email.com', password='top_secret')

    def test_follower_and_following_profile(self):
        """The user can have subscriptions and subscribers"""
        self.user.profile.follower.add(self.user2, self.user3)
        self.user.profile.following.add(self.user4)

        self.assertEqual(self.user.profile.follower.all()[0], self.user2)
        self.assertEqual(self.user.profile.follower.all()[1], self.user3)
        self.assertEqual(self.user.profile.following.all()[0], self.user4)


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@email.com', password='top_secret')
        self.user2 = User.objects.create_user(username='sergey', email='sergey@email.com', password='top_secret')
        self.user3 = User.objects.create_user(username='andrey', email='andrey@email.com', password='top_secret')

        Post.objects.create(author=self.user, image='media/avatar/iced_tea.jpeg', description='Post number one')

    def test_create_post_and_like(self):
        """Users can like the post"""
        post = Post.objects.get(pk=1)
        post.likes.add(self.user2, self.user3)

        self.assertEqual(post.author, self.user)
        self.assertEqual(post.likes.all()[0], self.user2)


class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@email.com', password='top_secret')
        self.post = Post.objects.create(author=self.user, image='media/avatar/iced_tea.jpeg', description='Post number one')

    def test_writing_comment(self):
        """The user can write comments on the post"""
        comment = Comment.objects.create(author=self.user, post=self.post, text='Nice post')

        self.assertEqual(self.post.comment_post.all()[0], comment)
        self.assertEqual(self.post.comment_post.all()[0].text, "Nice post")
