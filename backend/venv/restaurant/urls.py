from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]