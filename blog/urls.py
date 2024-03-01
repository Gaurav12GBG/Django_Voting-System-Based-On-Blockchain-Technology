from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.index,name="BlogHome"),
    path('blogpost/<int:id>', views.blogpost,name="blogPost"),
    path('search', views.search, name='search'),
]
