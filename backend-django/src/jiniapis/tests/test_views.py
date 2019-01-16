#_*_coding: utf-8 _*_
from django.contrib.auth.models import User
from django.test import TestCase

from .base import JiniapisBaseTest

# Create your tests here.
class JiniapisViewTests(TestCase):

    #smoke test
    # def test_smoke_test(self):
    #     assert 1 is not 1, "should be equal."

    def test_create_user_model(self):
        User.objects.create(
            username='logan'
        )
        assert User.objects.count() == 1, "should be equal"