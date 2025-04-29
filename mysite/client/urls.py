from django.urls import path

from . import views

urlpatterns = (
    path('', views.clients_list, name='clients_list'),
    path('add-client/', views.add_clients, name='add_clients'),
)