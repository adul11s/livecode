from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/', views.produk, name='produk'),

 
    # path('search/', SearchResultsView.as_view(), name="search"),
  
    # path('produk/<int:produkl_id>/', views.produkl_detail, name='produkl_detail'),
  
]


