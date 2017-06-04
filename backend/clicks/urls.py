from django.conf.urls import url

from clicks import views

urls = [
    url(r'^api/party?$', views.PartyList.as_view(), name='party-list'),
    url(r'^api/click?$', views.ClicksList.as_view(), name='click-list'),
]
