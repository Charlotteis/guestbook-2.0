from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Comment",          {"fields": ["comment"]}),
        ("Details",          {"fields": ["name", "email", "website"]}),
        ("Date Information", {"fields": ["date"]}),

    ]

admin.site.register(Post, PostAdmin)
