from django.urls import path

from . import views

app_name = "prf"
urlpatterns = [
    path('', views.prf, name = "prf")
]
