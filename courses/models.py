from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='basic')
    image = models.URLField(blank=True, null=True)
    course_url = models.URLField(blank=True, null=True)
    whatsapp_group = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name