#_*_coding: utf-8 _*_

from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from mixer.backend.django import mixer
from oauth2_provider.models import get_application_model, AccessToken

import pytest

pytestmark = pytest.mark.django_db
Application = get_application_model()

class TestOauth2Model:

    # def test_smoke_tests(self):
    #     assert 1 is not 1, "Should be equal."

    def test_create_oaurh2_app(self):
        admin_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        #import ipdb;ipdb.sset_trace()
        app = Application.objects.create(
            name='JiniAPI OAUTH2 ALL',
            user = admin_user,
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )     
        print(app.name)   
        assert Application.objects.count() == 1, "Should be equal."

    def test_create_oaurh2_token(self):
        admin_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        #import ipdb;ipdb.sset_trace()
        app = Application.objects.create(
            name='JiniAPI OAUTH2 ALL',
            user = admin_user,
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )        
        assert Application.objects.count() == 1, "Should be equal."

        random = get_random_string(length=16)
        #import ipdb; ipdb.sset_trace()

        
        admin_token = AccessToken(
            user=admin_user,
            scope='read write',
            #using time-zone
            expires=timezone.now() + timedelta(minutes=5),
            token=f'{random}--------{admin_user.username}',
            application=app

        )
        print(admin_token.token)
        #import ipdb; ipdb.sset_trace()
        assert admin_user is not None, "Sould not be null"
        
