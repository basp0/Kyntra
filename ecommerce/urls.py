from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),

    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/buyers/', views.admin_buyers, name='admin_buyers'),
    path('admin/buyers/<str:option>/', views.admin_buyers, name='admin_buyers'),
    path('admin/sellers/', views.admin_sellers, name='admin_sellers'),
    path('admin/sellers/<str:option>/', views.admin_sellers, name='admin_sellers'),
    path('admin/products/', views.admin_products, name='admin_products'),
    path('seller/all_products/', views.SellerAllView.as_view(), name='seller_all_products'),
    path('seller/all_products', views.SellerSearchView.as_view(), name='seller_searched_products'),
    path('seller/add_product/', views.addProductFormView, name='add_product'),
    path('seller/edit_product/<int:id>/', views.editProductFormView, name='edit_product'),
    # path('seller/delete_product/<int:id>/', views.deleteProductFormView, name='delete_product'),
    path('seller/registration/', views.seller_registration, name='seller_registration'),
    path('search/',views.SearchProductListView.as_view(),name="search_results"),
    path('logout/',views.logoutView, name ='logout')
]  
