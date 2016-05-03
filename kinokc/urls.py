from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^repertuar/$', views.repertuar, name='repertuar'),
    url(r'^bilety/$', views.bilety, name='bilety'),
    url(r'^rezerwacje/$', views.rezerwacje, name='rezerwacje'),
    url(r'^partnerzy/$', views.partnerzy, name='partnerzy'),
    url(r'^konatakt/$', views.kontakt, name='kontakt'),
]
