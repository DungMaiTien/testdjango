from django.urls import path

from . import views

app_name = "abm"
urlpatterns = [
    path('', views.abm, name = "abm"),
    path('abm/<int:pk>/',views.news_post, name = "news_post")
]
