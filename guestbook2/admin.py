from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Comment",          {"fields": ["comment"]}),
        ("Details",          {"fields": ["name", "email", "website"]}),
        ("Date Information", {"fields": ["date"]}),
    ]

    list_display = ("name", "date")
    list_filter = ["date"]
    search_fields = ["comment", "name"]

admin.site.register(Post, PostAdmin)
