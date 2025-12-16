import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kalvizhi_project.settings')
django.setup()

from courses.models import Course

# Create sample courses
courses_data = [
    {
        'name': 'Programming Basics',
        'description': 'Computer fundamentals, Internet usage, Logical thinking, Programming basics - Perfect for complete beginners',
        'whatsapp_group': 'https://chat.whatsapp.com/basics-group'
    },
    {
        'name': 'Web Development',
        'description': 'HTML – Build web pages, CSS – Design websites, JavaScript – Add actions to create interactive websites',
        'whatsapp_group': 'https://chat.whatsapp.com/webdev-group'
    },
    {
        'name': 'Python Programming',
        'description': 'Easy Python concepts, Real-life examples, Practice programs, Small projects to build your skills',
        'whatsapp_group': 'https://chat.whatsapp.com/python-group'
    },
    {
        'name': 'Backend Development',
        'description': 'Django framework, Database concepts, Login systems, Admin dashboards - Build complete applications',
        'whatsapp_group': 'https://chat.whatsapp.com/backend-group'
    }
]

for course_data in courses_data:
    course, created = Course.objects.get_or_create(
        name=course_data['name'],
        defaults={
            'description': course_data['description'],
            'whatsapp_group': course_data['whatsapp_group']
        }
    )
    if created:
        print(f"Created course: {course.name}")
    else:
        print(f"Course already exists: {course.name}")

print("Sample data setup complete!")