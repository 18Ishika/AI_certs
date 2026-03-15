from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        vendor = data.get("vendor")
        primary = data.get("primary_mapping")

        if primary:
            if VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            ).exists():
                raise serializers.ValidationError(
                    "Primary mapping already exists for this vendor"
                )

        return data