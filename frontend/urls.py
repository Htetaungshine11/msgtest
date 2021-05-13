from django.urls import path 
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path("room/<str:name>/",views.Chatroom.as_view(),name='chatroom'),
]
