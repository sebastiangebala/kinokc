from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^repertuar/$', views.repertuar, name='repertuar'),
    url(r'^bilety/$', views.bilety, name='bilety'),
    url(r'^rezerwacje/$', views.rezerwacje, name='rezerwacje'),
    url(r'^partnerzy/$', views.partnerzy, name='partnerzy'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
