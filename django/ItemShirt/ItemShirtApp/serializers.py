from rest_framework import serializers
from .models import Item, Size

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('size', 'price')


class ItemSerializer(serializers.ModelSerializer):
    size = SizeSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('item_id', 'brand_name', 'fabric', 'sku', 'fitting_type', 'imported', 'category_id', 'size')
