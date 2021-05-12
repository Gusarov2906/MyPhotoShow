
from django.db import models
import datetime
from django.contrib.auth.models import User


class Person(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to='img/profile')
    description = models.CharField(max_length=255)


class Post(models.Model):
    img = models.ImageField(upload_to='img/profile')
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    number_of_likes = models.IntegerField(default=0)
    date_of_publication = models.DateField(auto_now=True)
    liked_users = models.ManyToManyField(Person, through='PersonsLikedPosts'),


class UsersLikedPosts(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)



