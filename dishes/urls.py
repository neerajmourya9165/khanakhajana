
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:itemid>/', views.detail, name='detail'),
    path('<int:itemid>/ingredients', views.ingredients, name='ingredients'),
]