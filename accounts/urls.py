from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome_page),
    url(r'^about/$', views.about_profile, name='about_profile')
    ]

