from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, ProductCategoryViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += router.urls