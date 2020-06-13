from django.contrib import admin
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from .models import course, attendance, student, enrollment


@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ('Student', 'inst_student_id', 'first_name', 'last_name', 'phone',)
    list_filter = ('joining_date',)
    list_display_links = ['inst_student_id', ]
    list_editable = ('phone',)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_fee')
    search_fields = ('course_name', 'course_fee')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student')
    search_fields = ['student__first_name']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'presence')
    list_filter = ('date', )
    search_fields = ['student__first_name']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
