
from django.urls import path
from webapp.views import post

urlpatterns = [
    path('', post, name='post'),
]