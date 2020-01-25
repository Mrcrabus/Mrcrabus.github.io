from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('block/', views.block, name='blog-block'),
]
