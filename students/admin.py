from django.contrib import admin
from .models import course, attendance, student, enrollment
from django.contrib.auth.models import User, Group


class StudentAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

    list_display = ('inst_student_id', 'first_name', 'last_name', 'phone')
    list_filter = ('joining_date',)
    list_display_links = ['inst_student_id']
    list_editable = ('phone',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_fee')


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('course', 'student')


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'presence')


admin.site.register(student, StudentAdmin)
admin.site.register(course, CourseAdmin)
admin.site.register(attendance, AttendanceAdmin)
admin.site.register(enrollment, EnrollmentAdmin)

