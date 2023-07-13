from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Student(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"


class Subject(models.Model):
    title = models.CharField(max_length=120)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grade: {self.value} [{self.subject}]"

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"
