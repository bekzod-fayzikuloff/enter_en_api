from django.db import connection
from django.db.models import Avg
from rest_framework import serializers

from .models import Grade, Group, Student, Subject


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class GroupReportSerializer(serializers.ModelSerializer):
    avg_grades = serializers.SerializerMethodField()

    @staticmethod
    def get_avg_grades(group: Group):
        with connection.cursor() as cursor:
            query = """
                SELECT  r_subject.title, AVG(r_grade.value) AS grade__avg
                FROM reports_grade as r_grade
                    INNER JOIN reports_student as r_student
                        ON (r_grade.student_id = r_student.id)
                    INNER JOIN reports_subject as r_subject
                        ON (r_grade.subject_id = r_subject.id)
                WHERE r_subject.group_id = %s GROUP BY r_subject.title
            ;
            """
            cursor.execute(query, [group.pk])
            row = cursor.fetchall()
        grades = [{"subject": title, "avg": avg} for title, avg in row]
        return grades

    class Meta(GroupSerializer.Meta):
        pass


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        depth = 1


class StudentReportSerializer(serializers.ModelSerializer):
    avg_grades = serializers.SerializerMethodField()

    @staticmethod
    def get_avg_grades(student: Student):
        grades = [
            {"pk": pk, "title": title, "avg": avg}
            for pk, title, avg in Grade.objects.filter(student=student)
            .values_list("subject__pk", "subject__title")
            .annotate(Avg("value"))
        ]

        return grades

    class Meta:
        model = Student
        fields = "__all__"
        depth = 1


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
