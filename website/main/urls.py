from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('products', views.products),
    path('black_tshirt', views.black_tshirt),
    path('white_tshirt', views.white_tshirt),
    path('black_hoodie', views.black_hoodie),
    path('white_hoodie', views.white_hoodie),
]
