from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer
from drf_yasg.utils import swagger_auto_schema

class CourseCertificationMappingListCreateAPIView(APIView):

    def get(self, request):

        course_id = request.GET.get("course_id")

        mappings = CourseCertificationMapping.objects.all()

        if course_id:
            mappings = mappings.filter(course_id=course_id)

        serializer = CourseCertificationMappingSerializer(mappings, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer)
    def post(self, request):

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)
    
class CourseCertificationMappingDetailAPIView(APIView):

    def get_object(self, pk):

        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None


    def get(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        serializer = CourseCertificationMappingSerializer(mapping)

        return Response(serializer.data)


    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer)

    def put(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    def patch(self, request, pk):

        mapping = self.get_object(pk)

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


    @swagger_auto_schema(request_body=CourseCertificationMappingSerializer)

    def delete(self, request, pk):

        mapping = self.get_object(pk)

        if not mapping:
            return Response({"error": "Mapping not found"}, status=404)

        mapping.delete()

        return Response(status=204)