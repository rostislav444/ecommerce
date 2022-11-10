from rest_framework import viewsets, mixins, generics

from apps.product.models import Product
from apps.catalogue.serializers import CatalogueProductSerializer


class CatalogueProductViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                              mixins.DestroyModelMixin, viewsets.ViewSet):
    serializer_class = CatalogueProductSerializer

    def get_queryset(self):
        return Product.objects.all()
