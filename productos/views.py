from .models import ProductCategory, Products
from rest_framework import permissions, viewsets

from .serializers import ProductsSerializer, ProductCategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

