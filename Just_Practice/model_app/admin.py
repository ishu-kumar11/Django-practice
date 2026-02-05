from django.contrib import admin
from .models import Subject, Tag, Resources


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Resources)
class ResourceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "subject",
        "uploaded_by",
        "is_public",
        "created_at",
    )

    search_fields = ("title", "description", "uploaded_by__username")
    list_filter = ("category", "subject", "is_public", "created_at")
    ordering = ("-created_at",)

    filter_horizontal = ("tags",)  # ManyToMany field ko easy bana deta hai
