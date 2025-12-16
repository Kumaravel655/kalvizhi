from django.db import models
from django.core.validators import RegexValidator
from courses.models import Course

class User(models.Model):
    ELIGIBILITY_CHOICES = [
        ('eligible', 'Eligible'),
        ('not_eligible', 'Not Eligible'),
        ('pending_review', 'Pending Review'),
    ]
    
    username = models.CharField(max_length=150, unique=True, validators=[RegexValidator(r'^[a-z0-9]+$', 'Username must contain only lowercase letters and numbers')])
    password = models.CharField(max_length=128)  # Plain text
    email = models.EmailField()
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    eligibility = models.CharField(max_length=15, choices=ELIGIBILITY_CHOICES, default='pending_review')
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Application(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.course.name}"