from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('projects', views.projects, name='projects'),
    path('add_project', views.add_project, name='add_project'),
]