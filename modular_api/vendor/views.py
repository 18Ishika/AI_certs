from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Vendor
from .serializers import VendorSerializer
from drf_yasg.utils import swagger_auto_schema
class VendorListCreateAPIView(APIView):

    def get(self, request):

        vendors = Vendor.objects.filter(is_active=True)

        name = request.query_params.get('name')

        if name:
            vendors = vendors.filter(name__icontains=name)

        serializer = VendorSerializer(vendors, many=True)

        return Response(serializer.data)
    @swagger_auto_schema(request_body=VendorSerializer)
    def post(self, request):

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class VendorDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return None


    def get(self, request, pk):

        vendor = self.get_object(pk)

        if not vendor:
            return Response({"error": "Vendor not found"}, status=404)

        serializer = VendorSerializer(vendor)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=VendorSerializer)
    def put(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        vendor = self.get_object(pk)

        serializer = VendorSerializer(vendor, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=VendorSerializer)
    def delete(self, request, pk):

        vendor = self.get_object(pk)

        if not vendor:
            return Response({"error": "Vendor not found"}, status=404)

        vendor.is_active = False
        vendor.save()

        return Response({"message": "Vendor deactivated"}, status=200)    