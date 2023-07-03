from django.urls import path
from restaurant import views

app_name = 'restaurant'

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single_menu'),
    # path('menu/items/', views.MenuItemView.as_view(), name='menu_items'),
]