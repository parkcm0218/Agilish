#_*_coding: utf-8 _*_
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from oauth2_provider.models import get_application_model, AccessToken

#from django.test import TestCase
from django.urls import reverse
from rest_framework import status


import json
import pytest
from mixer.backend.django import mixer

from .base import JiniapisBaseTest

Application = get_application_model()
pytestmark = pytest.mark.django_db

# Create your tests here.
class JiniapisViewsTests(JiniapisBaseTest):

    #smoke test
    # def test_smoke_test(self):
    #     assert 1 is not 1, "should be equal."

      
    def test_create_fake_data_then_send_get_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / destroy / GET:PUT:DELETE


        admin_user = mixer.blend('auth.User', is_staff=True, is_superuser=True)
        #import ipdb;ipdb.sset_trace()
        app = Application.objects.create(
            name='JiniAPI OAUTH2 ALL',
            user = admin_user,
            client_type=Application.CLIENT_PUBLIC,
            authorization_grant_type=Application.GRANT_PASSWORD,
        )     
        assert Application.objects.count() == 1, "Should be equal"           

        random = get_random_string(length=16)
        #import ipdb; ipdb.sset_trace()

        
        admin_token = AccessToken.objects.create(
                user=admin_user,
                scope='read write',
                # 조금 까다롭네요 . . .
                expires=timezone.now() + timedelta(minutes=5),
                token=f'{random}---{admin_user.username}',
                application=app
        )

        #create 50 users
        for cnt in range(50):
            cnt = cnt
            mixer.blend('auth.User', is_active=True) 

        url = reverse('user-list')    
        #import ipdb;ipdb.sset_trace()
        
    
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {admin_token.token}'
        )           
        
        
        response = self.client.get(url, format='json')
        #print(response.content)
        assert response.status_code == status.HTTP_200_OK    

    
    
    def test_send_get_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / destroy / GET:PUT:DELETE
        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)

        url = reverse('user-list')
        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK

    def test_send_post_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / delete / GET:PUT:DELETE

        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)

        url = reverse('user-list')        
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test@naver.com',
            'is_active' : True,
        }

        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        ) 
        response = self.client.post(url, data=data, format='json')
        print(response.content)
        
        #import ipdb;ipdb.sset_trace()
        assert response.status_code == status.HTTP_201_CREATED
        #assert User.objects.get(pk=1).username == 'khlee'

        print(User.objects.get(pk=1).username)
    

    def test_send_retrive_update_destroy_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / delete / GET:PUT:DELETE

        admin_user = mixer.blend(
                'auth.User',
                is_staff=True,
                is_superuser=True)

        app = self.set_oauth2_app_by_admin(admin_user)
        access_token = self.get_token(admin_user, app)
        
        #create khlee user
        url = reverse('user-list')        
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test@naver.com',
            'is_active' : True,
        }

        self.client.credentials(
                HTTP_AUTHORIZATION=f'Bearer {access_token}'
        )

        response = self.client.post(url, data=data, format='json')
        print(response.content)
       
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.get(pk=2).username == 'khlee'

        #print(User.objects.get(pk=2).username)

        url = reverse('user-detail', args=[2])
        response = self.client.get(url, data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        #import ipdb; ipdb.sset_trace()
        #         
        url = reverse('user-detail', args=[2])  
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test123@naver.com',
            'is_active' : True,
        }             
        response = self.client.patch(url, data=json.dumps(data), content_type='application/json')
        #import ipdb; ipdb.sset_trace()
        print(response.content)
        print(User.objects.get(pk=2).email)
        print(User.objects.count())
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])               
        response = self.client.delete(url, content_type='application/json')
        print(response.content)
        print(User.objects.count())
        assert response.status_code == status.HTTP_204_NO_CONTENT


    
    