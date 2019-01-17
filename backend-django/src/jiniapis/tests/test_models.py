#_*_coding: utf-8 _*_
from django.test import TestCase
from django.contrib.auth.models import User

from mixer.backend.django import mixer

from .base import JiniapisBaseTest

# Create your tests here.
class JiniapisModelTests(TestCase):

    #smoke test
    # def test_smoke_test(self):
    #     assert 1 is not 1, "should be equal."

    def test_create_user_model(self):
        User.objects.create(
            username='logan'
        )
        assert User.objects.count() == 1, "Should be equal"

    def test_create_suuser_via_mixer(self):
    
        super_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        assert User.objects.count() is 1, "Should be equal"
        assert super_user.is_superuser is True, "Should be superuser"

    def test_create_user_via_mixer(self):        
        for cnt in range(50):
            cnt = cnt
            mixer.blend('auth.User')
        assert User.objects.count() is 50, "Should be equal"