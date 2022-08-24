from .views import ProductList, ProductDetail, ProductListDetailfilter, CreateProduct, EditProduct, AdminProductDetail, DeleteProduct
from django.urls import path

app_name = 'snooperspy_api'

urlpatterns = [
    path('', ProductList.as_view(), name='listproduct'),
    path('product/<str:pk>/', ProductDetail.as_view(), name='detailproduct'),
    path('search/', ProductListDetailfilter.as_view(), name='searchproduct'),
    # Product Admin URLs
    path('admin/create/', CreateProduct.as_view(), name='createproduct'),
    path('admin/edit/productdetail/<int:pk>/', AdminProductDetail.as_view(), name='admindetailproduct'),
    path('admin/edit/<int:pk>/', EditProduct.as_view(), name='editproduct'),
    path('admin/delete/<int:pk>/', DeleteProduct.as_view(), name='deleteproduct'),
]
