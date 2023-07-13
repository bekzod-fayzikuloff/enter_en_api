from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.utils.models import include_queryset

from .models import Grade, Group, Student, Subject
from .serializers import (
    GradeSerializer,
    GroupReportSerializer,
    GroupSerializer,
    StudentListSerializer,
    StudentReportSerializer,
    StudentSerializer,
    SubjectSerializer,
)


class GroupViewSet(ModelViewSet):
    queryset = include_queryset(Group)
    serializer_class = GroupSerializer

    @action(methods=["GET"], detail=True)
    def reports(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        serializers = {"reports": GroupReportSerializer}
        return serializers.get(self.action, self.serializer_class)


class StudentViewSet(ModelViewSet):
    queryset = include_queryset(Student)
    serializer_class = StudentSerializer

    @action(methods=["GET"], detail=True)
    def reports(self, request: Request, *args, **kwargs) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def get_serializer_class(self):
        serializers = {"list": StudentListSerializer, "reports": StudentReportSerializer}
        return serializers.get(self.action, self.serializer_class)


class SubjectViewSet(ModelViewSet):
    queryset = include_queryset(Subject)
    serializer_class = SubjectSerializer


class GradeViewSet(ModelViewSet):
    queryset = include_queryset(Grade)
    serializer_class = GradeSerializer
