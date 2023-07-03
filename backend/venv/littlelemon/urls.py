from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from restaurant.views import BookingViewSet
from restaurant import views

router = DefaultRouter()
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]