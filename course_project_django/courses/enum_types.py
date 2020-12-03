from core.base_enum import BaseEnum


class RolesType(BaseEnum):
    STUDENT = 'student'
    TEACHER = 'teacher'


class HomeworkType(BaseEnum):
    PENDING = 'pending'
    ACTIVE = 'active'
    FINISHED = 'finished'


class CourseType(BaseEnum):
    PENDING = 'pending'
    ACTIVE = 'active'
    FINISHED = 'finished'
