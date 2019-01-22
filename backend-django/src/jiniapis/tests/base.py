#_*_coding: utf-8 _*_
from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.crypto import get_random_string

from rest_framework.test import APITestCase
from oauth2_provider.models import get_application_model, AccessToken

import pytest
from mixer.backend.django import mixer

Application = get_application_model()
pytestmark = pytest.mark.django_db

# Create your tests here.
class JiniapisBaseTest(APITestCase):

    #smoke test
    # def test_smoke_test(self):
    #     assert 1 is not 1, "should be equal."

    def test_create_user_model(self):
        User.objects.create(
            username='khlee'
        )
        assert User.objects.count() == 1, "Should be equal"

    def set_oauth2_app_by_admin(self, user):
        app = Application.objects.create(
                name='SuperAPI OAUTH2 APP',
                user=user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD,
        )
        return app

    def get_token(self, access_user, app):
        random = get_random_string(length=1024)
        access_token = AccessToken.objects.create(
                user=access_user,
                scope='read write',
                expires=timezone.now() + timedelta(minutes=5),
                token=f'{random}---{access_user.username}',
                application=app
        )
        return access_token.token