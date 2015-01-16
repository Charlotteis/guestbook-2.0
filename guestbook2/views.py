from django.shortcuts import render

from .models import Post


def index(request):
    """ Renders the guestbook2/index.html template
    """

    latest_posts_list = Post.objects.order_by("-date")[:10]
    context = {"latest_posts_list": latest_posts_list}

    return render(request, "guestbook2/index.html", context)
