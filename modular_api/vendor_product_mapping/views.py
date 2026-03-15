from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer
from drf_yasg.utils import swagger_auto_schema
class VendorProductMappingListCreateAPIView(APIView):


    def get(self, request):

        vendor_id = request.GET.get("vendor_id")

        mappings = VendorProductMapping.objects.all()

        if vendor_id:
            mappings = mappings.filter(vendor_id=vendor_id)

        serializer = VendorProductMappingSerializer(mappings, many=True)

        return Response(serializer.data)


    @swagger_auto_schema(request_body=VendorProductMappingSerializer)
    def post(self, request):

        serializer = VendorProductMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
    
class VendorProductMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return VendorProductMapping.objects.get(pk=pk)
        except VendorProductMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = VendorProductMappingSerializer(mapping)

        return Response(serializer.data)


    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = VendorProductMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def delete(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        mapping.delete()

        return Response(status=204)