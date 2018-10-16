from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signin/?$', views.SignInUp.as_view(), name='signinup'),
]
