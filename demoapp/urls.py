from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name="demo")
    #path('add/', views.addition, name="addition")
    #path('Detail/', views.Detail, name="Detail"),
    #path('Thanks/', views.demo2, name="demo2")

]
