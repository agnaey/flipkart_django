from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sec/<id>', views.secpage),
]