from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Certification
from .serializers import CertificationSerializer
from drf_yasg.utils import swagger_auto_schema


class CertificationListCreateAPIView(APIView):

    def get(self, request):
        certifications = Certification.objects.all()
        serializer = CertificationSerializer(certifications, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer)
    def post(self, request):
        serializer = CertificationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)


class CertificationDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            return None

    def get(self, request, pk):
        certification = self.get_object(pk)

        if not certification:
            return Response({"error": "Certification not found"}, status=404)

        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CertificationSerializer)

    def put(self, request, pk):
        certification = self.get_object(pk)

        serializer = CertificationSerializer(certification, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        certification = self.get_object(pk)

        serializer = CertificationSerializer(certification, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
    
    @swagger_auto_schema(request_body=CertificationSerializer)

    def delete(self, request, pk):
        certification = self.get_object(pk)

        if not certification:
            return Response({"error": "Certification not found"}, status=404)

        certification.delete()
        return Response(status=204)