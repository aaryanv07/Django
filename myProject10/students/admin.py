from django.contrib import admin
from .models import Student
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','city']
    search_fields=['name','age','city']
    list_filter=('age','city','age')
    ordering=('name',) # tuple is mandatory 
