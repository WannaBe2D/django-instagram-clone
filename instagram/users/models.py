from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default/default_pic.jpeg')
    bio = models.TextField(blank=True)

    follower = models.ManyToManyField(User, related_name='followers_profile', blank=True)
    following = models.ManyToManyField(User, related_name='following_profile', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/%Y/%m/%d')
    description = models.CharField(max_length=500, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.author.username


class Comment(models.Model):
    author = models.ForeignKey(User, related_name='author_comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_post')
    text = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
