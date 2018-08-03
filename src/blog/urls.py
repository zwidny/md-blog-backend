from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogView.as_view()),
    url(r'^(?P<id>\d+)$', views.BlogDetail.as_view()),
]
