from django.contrib import admin
from .models import User, Application

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'eligibility', 'created_at']
    list_filter = ['eligibility', 'created_at']
    search_fields = ['username', 'full_name', 'email']
    actions = ['make_eligible', 'make_not_eligible', 'make_pending_review']
    
    def make_eligible(self, request, queryset):
        queryset.update(eligibility='eligible')
    make_eligible.short_description = "Mark selected users as eligible"
    
    def make_not_eligible(self, request, queryset):
        queryset.update(eligibility='not_eligible')
    make_not_eligible.short_description = "Mark selected users as not eligible"
    
    def make_pending_review(self, request, queryset):
        queryset.update(eligibility='pending_review')
    make_pending_review.short_description = "Mark selected users as pending review"

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'status', 'applied_at']
    list_filter = ['status', 'course', 'applied_at']
    search_fields = ['user__username', 'user__full_name']