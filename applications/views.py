from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from .models import User, Application
from .serializers import UserSerializer, ApplicationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username=request.data['username']).exists():
                return Response({'error': 'Username already exists'}, status=400)
            serializer.save()
            return Response({'message': 'User created successfully'})
        return Response(serializer.errors, status=400)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=401)
    
    @action(detail=False, methods=['post'])
    def admin_login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = User.objects.get(username=username, password=password, is_admin=True)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'Invalid admin credentials'}, status=401)
    
    @action(detail=False, methods=['post'])
    def bulk_update(self, request):
        field = request.data.get('field')
        value = request.data.get('value')
        user_ids = request.data.get('user_ids', [])
        
        if user_ids:
            User.objects.filter(id__in=user_ids).update(**{field: value})
        else:
            User.objects.all().update(**{field: value})
        
        return Response({'message': 'Users updated successfully'})

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    
    @action(detail=False, methods=['get'])
    def user_applications(self, request):
        user_id = request.query_params.get('user_id')
        if user_id:
            applications = Application.objects.filter(user_id=user_id)
            serializer = self.get_serializer(applications, many=True)
            return Response(serializer.data)
        return Response({'error': 'User ID required'}, status=400)