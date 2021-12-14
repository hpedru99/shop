from django.conf.urls import url
from . import views


app_name = 'shop'

urlpatterns = [
    url('', views.product_list, name='product_list'),
    url('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    url('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
