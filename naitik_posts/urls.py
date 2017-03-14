from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [

    url(r'^$', "naitik_posts.views.post_list"),
    url(r'^create/$', "naitik_posts.views.post_create"),
    url(r'^delete/$', "naitik_posts.views.post_delete"),
    url(r'^update/$', "naitik_posts.views.post_update"),
    url(r'^detail/$', "naitik_posts.views.post_details"),
]
