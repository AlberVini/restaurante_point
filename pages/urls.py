from . import views
from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('sobre', views.AboutPageView.as_view(), name='about'),
    # client urls
    path('cliente-area/', views.client_setup, name='client_setup'),
    path('editar-cliente/', views.edit_client, name='edit_client'),
    path('cliente-pedidos/', views.ListOrders.as_view(), name='client_orders'),
    # restaurante urls
    path('restaurante-area/', views.restaurant_setup, name='restaurant_setup'),
    path('adicionar-produto/', views.add_product, name='add_product'),
    path('lista-produtos/', views.list_product, name='list_product'),
    path('editar-produto/<int:id>', views.edit_product, name='product_edit'),
    path('deletar-produto/<int:id>', views.delete_product, name='product_delete'),
    path('editar-restaurante/', views.edit_restaurant, name='edit_restaurant'),
    path('restaurante-pedidos/', views.restaurant_orders, name='restaurant_orders'),
]
