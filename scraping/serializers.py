from rest_framework import serializers

from scraping.models import YarnProduct


class YarnProductSerializer(serializers.ModelSerializer):
    resources = serializers.StringRelatedField(many=True)

    class Meta:
        model = YarnProduct
        fields = ['name', 'brand', 'needle_size', 'composition', 'lowest_price', 'historical_lowest_price', 'resources']
