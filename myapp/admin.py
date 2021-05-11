from django.contrib import admin

from .models import Person, Post, UsersLikedPosts

admin.site.register(Person)
admin.site.register(Post)
admin.site.register(UsersLikedPosts)

# Register your models here.
