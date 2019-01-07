from django.conf.urls import url
from django.contrib import admin
from . import views as songs_views

urlpatterns = [
    url(r'^$', songs_views.song_list),
    url(r'^create/$', songs_views.song_create),
    url(r'^(?P<id>\d+)/$', songs_views.song_detail, name='detail'),
    url(r'^update/$', songs_views.song_update),
    url(r'^delete/$', songs_views.song_delete),
]
