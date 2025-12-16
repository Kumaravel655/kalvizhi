from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'course_url', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'image', 'course_url', 'whatsapp_group']