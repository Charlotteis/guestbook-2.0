from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = "guestbook2/index.html"
    context_object_name = "latest_posts_list"

    def get_queryset(Self):
        """ Return the last 10 submitted posts
            (not including those to be published in the future)"""
        return Post.objects.filter(
            date__lte=timezone.now()
            ).order_by("-date")[:10]


class FormView(generic.TemplateView):
    template_name = "guestbook2/form.html"


def add_post(request):
    """ Checks form input for valid data and adds post to database """

    # If a name was submitted, add it to the post or serve an error
    if request.POST["name"] == "":
        return render(request, "guestbook2/form.html", {
            "error_message": "You need to input a name!",
        })
    else:
        post_name = request.POST["name"]

    # If a comment was submitted, add it to the post or server an error
    if request.POST["comment"] == "":
        return render(request, "guestbook2/form.html", {
            "error_message": "You need to input a comment!",
        })
    else:
        post_comment = request.POST["comment"]

    # Check to make sure the URL is valid, if it isn't, throw an error.
    validate = URLValidator()
    post_website = request.POST["website"]
    if post_website != "":
        try:
            validate(request.POST["website"])
        except ValidationError:
            return render(request, "guestbook2/form.html", {
                "error_message": "You've entered an invalid URL, \
                                  make sure it starts with http://"
            })
        else:
            post_website = request.POST["website"]

    post_email = request.POST["email"]
    post_date = timezone.now()

    post = Post(name=post_name, comment=post_comment, email=post_email,
                website=post_website, date=post_date
                )

    post.save()

    return HttpResponseRedirect("/")
