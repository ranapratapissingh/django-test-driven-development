from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.EntryDetail.as_view(), name='entry_detail'),
]