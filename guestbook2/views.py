from django.shortcuts import render
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "guestbook2/index.html"
    context_object_name = "latest_posts_list"

    def get_queryset(Self):
        """ Return the last 10 submitted posts """
        return Post.objects.order_by("-date")[:10]
