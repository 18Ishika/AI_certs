from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductCourseMapping
from drf_yasg.utils import swagger_auto_schema

from .serializers import ProductCourseMappingSerializer
class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):

        product_id = request.GET.get("product_id")

        mappings = ProductCourseMapping.objects.all()

        if product_id:
            mappings = mappings.filter(product_id=product_id)

        serializer = ProductCourseMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer)
    def post(self, request):

        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)
class ProductCourseMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return ProductCourseMapping.objects.get(pk=pk)
        except ProductCourseMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = ProductCourseMappingSerializer(mapping)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer)
    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = ProductCourseMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    @swagger_auto_schema(request_body=ProductCourseMappingSerializer)
    def delete(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        mapping.delete()

        return Response(status=204)