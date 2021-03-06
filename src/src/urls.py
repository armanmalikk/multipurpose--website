"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from multi.views import main_body,about,services,portfolio,page,blog,contact

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_body, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^services/$', services, name='services'),
    url(r'^portfolio/$', portfolio, name='portfolio'),
    url(r'^page/$', page, name='page'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^contact/$', contact, name='contact'),
]
