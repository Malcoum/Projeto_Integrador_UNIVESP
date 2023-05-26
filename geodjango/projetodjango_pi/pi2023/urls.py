from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index_exemplo, name='index-exemplo'),
    path('', views.index, name='index'),
    path('sobre-o-projeto/', views.sobre_o_projeto, name='sobre-o-projeto'),
    path('universidade/', views.universidade, name='universidade'),
]
