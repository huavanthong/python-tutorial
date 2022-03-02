from django.urls import path
from . import views
urlpatterns = [
    path('hello1', views.hello1, name='hello1'),
    path('hello2', views.hello2, name='hello2'),
    path('hello3', views.hello3, name='hello3'),
    path('hello4', views.hello2, name='hello4'),
]
