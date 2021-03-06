from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),


    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/buyers/', views.admin_buyers, name='admin_buyers'),
    path('admin/buyers/<str:option>/', views.admin_buyers, name='admin_buyers'),
    path('admin/removebuyers/', views.admin_removebuyer, name='admin_removebuyer'),

    path('admin/sellers/', views.admin_sellers, name='admin_sellers'),
    path('admin/sellers/<str:option>/', views.admin_sellers, name='admin_sellers'),
    path('admin/selleractions/', views.admin_selleractions, name='admin_selleractions'),

    path('admin/products/', views.admin_products, name='admin_products'),
    path('admin/products/<str:option>/', views.admin_products, name='admin_products'),
    path('admin/addproducts/', views.admin_addproduct, name='admin_addproduct'),
    path('admin/removeproducts/', views.admin_removeproduct, name='admin_removeproduct'),
    path('admin/logs/', views.admin_logs, name='admin_logs'),



    path('seller/unapproved', views.unapproved_seller,name="unapproved"),
    path('seller/rejected', views.rejected_seller,name="rejected"),
    path('seller/all_products/', views.showAllProducts, name='seller_all_products'),
    path('seller/add_product/', views.addProductFormView, name='add_product'),
    path('seller/edit_product/<pk>/', views.EditProductView.as_view(), name='edit_product'),
    path('seller/removeproducts/<pk>', views.RemoveProductView.as_view(), name='seller_removeproduct'),
    path('seller/registration/', views.seller_registration, name='seller_registration'),
    path('search/',views.SearchProductListView.as_view(),name="search_results"),
    path('checkout/complete/', views.payment_complete, name='payment_complete'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name='product'),
    path('purchase/',views.Purchase,name="purchase_endpoint"),
    path('logout/',views.logoutView, name ='logout')
]  
