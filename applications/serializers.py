from rest_framework import serializers
from .models import User, Application
from courses.serializers import CourseSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    course_details = CourseSerializer(source='course', read_only=True)
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'