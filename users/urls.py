from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup'),
    path('cliente/', views.ClientSignUp.as_view(), name='client_signup'),
    path('restaurante/', views.RestaurantSignUp.as_view(), name='restaurant_signup'),
]