from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.cache import cache_page

from products.views import (IndexView, ProductsListView, basket_add,
                            basket_remove)

app_name = 'products'
urlpatterns = [
    path('', cache_page(30)(ProductsListView.as_view()), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]