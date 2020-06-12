from django.contrib import admin
from .models import course, attendance, student, enrollment
from django.contrib.auth.models import User, Group

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

    list_display = ('inst_student_id', 'first_name', 'last_name', 'phone',)
    list_filter = ('joining_date',)
    list_display_links = ['inst_student_id',]
    list_editable = ('phone',)


@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_fee')


@admin.register(enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student')
    list_filter = ('course', 'student')


@admin.register(attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'presence')
    list_filter = ('date', 'student')
