from django.conf.urls import patterns, url

from guestbook2 import views

urlpatterns = patterns("",
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^add_post/$", views.FormView.as_view(), name="add_post"),
    url(r"^submit/$", views.add_post, name="submit")
)
