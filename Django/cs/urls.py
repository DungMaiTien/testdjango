from django.urls import path

from . import views

app_name = "cs"
urlpatterns = [
    path('', views.cs, name = "cs")
]
