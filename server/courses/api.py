from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from accounts.models import AdvancedUser


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = AdvancedUser.objects.filter(is_staff=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TeacherSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CoursesManySerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Если пингуется по пути /api/course/id, то возвращаться будет с полем lessons_in_course
        """
        pk = int(kwargs["pk"])
        queryset = Courses.objects.filter(id=pk)
        serializer = CoursesSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        """
        Переопределяется для того, чтобы при попытке сделать PUT/DELETE не выкидывало 404
        :return:
        """
        if self.request.method == "PUT" or self.request.method == "DELETE":
            return Courses.objects.all()
        else:
            return Courses.objects.filter(is_deleted=False)


class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LessonsSerializer
