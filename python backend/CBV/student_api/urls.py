from django.urls import path

from .views import StudentList

urlpatterns = [
    path('student_list/', StudentList.as_view())
]