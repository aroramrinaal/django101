from unicodedata import name
from django.urls import path

from . import views



urlpatterns = [

    path("hello-world/",views.hello, name = "hello"),
    path("greet/",views.greet, name="hello,mrinaal"),
    path("welcome/<str:name>",views.welcome,name= "welcome"),
    path("hello/",views.html,name= "hellllo")
]