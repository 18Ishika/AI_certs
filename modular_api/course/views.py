from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course
from .serializers import CourseSerializer
from drf_yasg.utils import swagger_auto_schema


class CourseListCreateAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CourseSerializer)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=400)


class CourseDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return None

    def get(self, request, pk):
        course = self.get_object(pk)

        if not course:
            return Response({"error": "Course not found"}, status=404)

        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=CourseSerializer)

    def put(self, request, pk):
        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        course = self.get_object(pk)

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)
 
    
    @swagger_auto_schema(request_body=CourseSerializer)

    def delete(self, request, pk):
        course = self.get_object(pk)

        if not course:
            return Response({"error": "Course not found"}, status=404)

        course.delete()
        return Response(status=204)