from django.urls import path
from . import views

urlpatterns = [
  path('hello1/', views.say_Hello1),
  path('hello2/', views.say_Hello2)

]