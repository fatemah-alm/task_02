from django.urls import path
from . import views

#urlConf
urlpatterns = [
    path('hello-world/', views.helloworld)
]