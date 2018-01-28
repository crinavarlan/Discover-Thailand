from django.test import TestCase
from .models import BlogPost


class BlogPostTests(TestCase):
    """
    Here we'll define the tests
    that we'll run against our BlogPost model
    """


def test_str(self):
    test_title = BlogPost(title='My Latest Blog BlogPost')
    self.assertEqual(str(test_title),
                     'My Latest Blog BlogPost')
