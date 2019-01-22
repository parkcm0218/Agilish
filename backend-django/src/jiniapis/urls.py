#_*_coding: utf-8 _*_

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from jiniapis.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]