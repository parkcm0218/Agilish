#_*_coding: utf-8 _*_
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework import status


from mixer.backend.django import mixer

from .base import JiniapisBaseTest

# Create your tests here.
class JiniapisViewsTests(TestCase):

    #smoke test
    # def test_smoke_test(self):
    #     assert 1 is not 1, "should be equal."

      
    def test_create_fake_data_then_send_get_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / destroy / GET:PUT:DELETE

        #create 50 users

        for cnt in range(50):
            cnt = cnt
            mixer.blend('auth.User', is_active=True) 

        url = reverse('user-list')        
        response = self.client.get(url, format='json')
        #print(response.content)
        assert response.status_code == status.HTTP_200_OK    

    
    
    def test_send_get_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / destroy / GET:PUT:DELETE

        url = reverse('user-list')        
        response = self.client.get(url, format='json')
        #import ipdb;ipdb.sset_trace()
        assert response.status_code == status.HTTP_200_OK

    def test_send_post_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / delete / GET:PUT:DELETE

        url = reverse('user-list')        
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test@naver.com',
            'is_active' : True,
        }
        response = self.client.post(url, data=data, format='json')
        print(response.content)
        print(User.objects.get(pk=1).username)
        #import ipdb;ipdb.sset_trace()
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.get(pk=1).username == 'khlee'
    
    def test_send_retrive_update_destroy_request_via_user_viewset(self):
        # list GET : POST
        # retrive / patch / destroy / GET:PUT:DELETE

        #create khlee user
        url = reverse('user-list')        
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test@naver.com',
            'is_active' : True,
        }
        response = self.client.post(url, data=data, format='json')
        print(response.content)
        print(User.objects.get(pk=1).username)
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.get(pk=1).username == 'khlee'

        url = reverse('user-detail', args=[1])               
        response = self.client.get(url, data=data, format='json')
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])  
        data={
            'username' : 'khlee',
            'password' : '12345',
            'email' : 'test123@naver.com',
            'is_active' : True,
        }             
        response = self.client.patch(url, data=data, content_type='application/json')
        print(response.content)
        print(User.objects.get(pk=1).email)
        print(User.objects.count())
        assert response.status_code == status.HTTP_200_OK

        url = reverse('user-detail', args=[1])               
        response = self.client.delete(url, content_type='application/json')
        print(response.content)
        print(User.objects.count())
        assert response.status_code == status.HTTP_204_NO_CONTENT


    
    