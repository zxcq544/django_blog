import datetime
from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from .models import Post


class PostMethodTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertEqual(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() should return False for posts whose
        pub_date is older than 1 day.
        """

        time = timezone.now() - datetime.timedelta(days=30)
        old_post = Post(pub_date=time)
        self.assertEqual(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() should return True for posts whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_post = Post(pub_date=time)
        self.assertEqual(recent_post.was_published_recently(), True)
