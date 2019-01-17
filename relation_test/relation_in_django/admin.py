from django.contrib import admin
from .models import *
# Register your models here.

#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['sname' ,'age','email','loc']
#
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['student','cname','fee']
#
# admin.site.register(Student ,StudentAdmin)
# admin.site.register(Course ,CourseAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['aname','loc']


class BookAdmin(admin.ModelAdmin):
    list_display = ['get_authors','bname','bcost']


admin.site.register(Author ,AuthorAdmin)
admin.site.register(Book ,BookAdmin)
