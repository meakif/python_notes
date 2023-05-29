from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView


class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer =StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
