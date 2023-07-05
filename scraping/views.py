from rest_framework import viewsets

from scraping.models import YarnProduct
from scraping.serializers import YarnProductSerializer


class YarnProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows to view scraped yarn products.
    """
    queryset = YarnProduct.objects.all().order_by('updated_at')
    serializer_class = YarnProductSerializer
