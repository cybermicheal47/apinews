from django.urls import path
from . import views
urlpatterns =[
    path('', views.home, name="index"),  
     path('next', views.loadcontent, name="Loadcontent"),
]