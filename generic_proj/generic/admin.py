from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Post, Photo, Comment


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'content_type', 'object_id']
