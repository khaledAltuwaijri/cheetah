from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.getSongRequest, name='song_request')
]
