from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ContactsView, ProductDetailView, ProductCreateView, ProductDeleteView,
                           ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [path("", ProductListView.as_view(), name='product_list'),
               path("contacts/", ContactsView.as_view(), name='contacts'),
               path("product/<int:pk>/", ProductDetailView.as_view(), name='product_detail'),
               path("product/update/<int:pk>/", ProductUpdateView.as_view(), name='product_update'),
               path('product/create/', ProductCreateView.as_view(), name='product_create'),
               path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
               ]
