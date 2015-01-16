import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from guestbook2.models import Post


def create_post(name, comment, days):
    """
    Creates a Post with the given 'name' and 'comment'
    """
    post_date = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(name=name, comment=comment, date=post_date)


class PostViewTests(TestCase):
    def test_index_view_with_no_posts(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse("guestbook2:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no posts to display!")
        self.assertQuerysetEqual(response.context["latest_posts_list"], [])

    def test_index_view_with_a_past_post(self):
        """
        Posts with a date in the past should be displayed on the index page.
        """
        create_post(name="Charlotte", comment="test_index_past_post", days=-30)
        response = self.client.get(reverse("guestbook2:index"))
        self.assertQuerysetEqual(
            response.context["latest_posts_list"],
            ["<Post: test_index_past_post>"]
        )

    def test_index_view_with_a_future_post(self):
        """
        Posts with a date in the future should not be displayed on the index.
        """
        create_post(name="Charlotte", comment="test_index_future_post", days=30)
        response = self.client.get(reverse("guestbook2:index"))
        self.assertContains(response, "There are no posts to display!",
                            status_code=200)
        self.assertQuerysetEqual(response.context["latest_posts_list"], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_post(name="Charlotte", comment="test_index_past", days=-30)
        create_post(name="Charlotte", comment="test_future_post", days=30)
        response = self.client.get(reverse("guestbook2:index"))
        self.assertQuerysetEqual(
            response.context["latest_posts_list"],
            ["<Post: test_index_past>"]
        )

    def test_index_view_with_two_past_posts(self):
        """
        The index page may display multiple posts.
        """
        create_post(name="Charlotte", comment="Past Q1", days=-30)
        create_post(name="Charlotte", comment="Past Q2", days=-10)
        response = self.client.get(reverse("guestbook2:index"))
        self.assertQuerysetEqual(
            response.context["latest_posts_list"],
            ["<Post: Past Q2>", "<Post: Past Q1>"]
        )

    def test_index_view_only_displays_ten_posts(self):
        """
        Make sure the index page only displays ten posts.
        """
        create_post(name="Charlotte", comment="Past Q1", days=-30)
        create_post(name="Charlotte", comment="Past Q2", days=-30)
        create_post(name="Charlotte", comment="Past Q3", days=-30)
        create_post(name="Charlotte", comment="Past Q4", days=-30)
        create_post(name="Charlotte", comment="Past Q5", days=-30)
        create_post(name="Charlotte", comment="Past Q6", days=-30)
        create_post(name="Charlotte", comment="Past Q7", days=-30)
        create_post(name="Charlotte", comment="Past Q8", days=-30)
        create_post(name="Charlotte", comment="Past Q9", days=-30)
        create_post(name="Charlotte", comment="Past Q10", days=-30)
        create_post(name="Charlotte", comment="Past Q11", days=-30)
        create_post(name="Charlotte", comment="Past Q12", days=-30)
        response = self.client.get(reverse("guestbook2:index"))
        self.assertQuerysetEqual(
            response.context["latest_posts_list"],
            ["<Post: Past Q12>", "<Post: Past Q11>", "<Post: Past Q10>",
             "<Post: Past Q9>", "<Post: Past Q8>", "<Post: Past Q7>",
             "<Post: Past Q6>", "<Post: Past Q5>", "<Post: Past Q4>",
             "<Post: Past Q3>"]
        )
