from django.contrib import admin
from django.urls import path, include
from comm import views

urlpatterns = [
    path('', views.ServerList.as_view(), name="server-list"),
    path('search/', views.ServerSearchView.as_view(), name="server-search"),
    path('servers/<int:sid>/', views.ServerDetailView.as_view(), name="picture-update"),
    path('<int:sid>/channel/', views.ChannelList.as_view(), name="channel-list"),
    path('channel/<int:cid>/', views.ChanneLDetailView().as_view(), name="channel-detail"),
    path('channel/<int:cid>/message/', views.MessageList.as_view(), name="message-list"),
    path('message/<int:mid>/', views.MessageDetail.as_view(), name="message-detail"),
]
