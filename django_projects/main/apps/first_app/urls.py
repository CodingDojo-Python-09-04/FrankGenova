from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^test$', views.test),
    url(r'^ground$$', views.ground_up)
]
