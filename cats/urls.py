from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('api_random_cat/', views.api_random_cat, name="api_random_cat"),
]