from django import urls
from django.urls import path
from . import views

app_name='cb'
urlpatterns = [
    path('book/', views.BookMetaList.as_view(), name = 'booklist'),
    path('usr/', views.UsrList.as_view(), name = 'usrlist'),
    path('rps/', views.RpsList.as_view(), name = 'rpslist'),
    path('rps/form/', views.rps_new, name='rpsform'),
]
