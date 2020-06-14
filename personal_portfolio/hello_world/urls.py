from django.urls import path
from hello_world import views

urlpatterns = [
    path('', views.hello_w, name='hello_world'),
]
