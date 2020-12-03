import os

from django.db import models

from users.models import User
from courses.enum_types import RolesType, HomeworkType, CourseType


def get_upload_path(self, filename):
    return os.path.join(self.image_path(), filename)


def get_upload_path_doc(self, filename):
    return os.path.join(self.doc_path(), filename)


class Participant(models.Model):
    user = models.ForeignKey(User, models.CASCADE)

    headshot = models.ImageField(upload_to=get_upload_path, blank=True)
    role = models.CharField(
        max_length=10,
        choices=RolesType.items(),
        default=RolesType.STUDENT.value
    )

    def image_path(self):
        return os.path.join(f'participant_headshot/{self.id}')

    class Meta:
        db_table = 'participant'
        ordering = ('user',)


class Course(models.Model):
    owner = models.ForeignKey(Participant, models.CASCADE, related_name='owner')
    title = models.CharField(blank=True, max_length=256)
    logo = models.ImageField(upload_to=get_upload_path, blank=True)
    subject = models.CharField(blank=True, max_length=256)
    status = models.CharField(
        max_length=10,
        choices=CourseType.items(),
        default=CourseType.PENDING.value
    )
    status_date = models.DateField(auto_now_add=True)

    def image_path(self):
        return os.path.join(f'course_logo/{self.id}')

    class Meta:
        db_table = 'course'
        ordering = ('owner',)


class CourseParticipant(models.Model):
    participant = models.ForeignKey(Participant, models.CASCADE, related_name='course_participant')
    course = models.ForeignKey(Course, models.CASCADE)

    class Meta:
        db_table = 'course_participant'
        ordering = ('participant',)


class Lecture(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, related_name='course')
    topic = models.CharField(blank=True, max_length=256)
    document = models.FileField(upload_to=get_upload_path_doc, blank=True)
    start_date = models.DateField()

    def doc_path(self):
        return os.path.join(f'documents/{self.course_id}/{self.id}')

    class Meta:
        db_table = 'lecture'
        ordering = ('course',)


class LectureCommentary(models.Model):
    lecture = models.ForeignKey(Lecture, models.CASCADE, related_name='mark')
    text = models.CharField(blank=True, max_length=256)

    class Meta:
        db_table = 'LectureCommentary'
        ordering = ('lecture',)


class Homework(models.Model):
    lecture = models.ForeignKey(Lecture, models.CASCADE, related_name='lecture')
    task = models.TextField(max_length=255, blank=True)
    status = models.CharField(
        max_length=10,
        choices=HomeworkType.items(),
        default=HomeworkType.PENDING.value
    )

    class Meta:
        db_table = 'homework'
        ordering = ('lecture',)


class Mark(models.Model):
    homework = models.ForeignKey(Homework, models.CASCADE, related_name='homework')
    student = models.ForeignKey(Participant, models.CASCADE, related_name='student')
    result = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'mark'
        ordering = ('homework',)


class MarkCommentary(models.Model):
    mark = models.ForeignKey(Mark, models.CASCADE, related_name='mark')
    text = models.CharField(blank=True, max_length=256)

    class Meta:
        db_table = 'MarkCommentary'
        ordering = ('mark',)
