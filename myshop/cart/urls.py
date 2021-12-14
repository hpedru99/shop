from django.conf.urls import url
from . import views
from django.utils.translation import gettext_lazy as _


app_name = 'cart'
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(_(r'^add/(?P<product_id>\d+)/$'), views.cart_add, name='cart_add'),
    url(_(r'^remove/(?P<product_id>\d+)/$'), views.cart_remove, name='cart_remove'),
]
