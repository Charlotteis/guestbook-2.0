from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, null=True, blank=True)
    website = models.CharField(max_length=100, blank=True)
    comment = models.TextField()
    date = models.DateTimeField("date published")

    def __str__(self):
        return "{0} - {1}".format(self.name, self.date)
