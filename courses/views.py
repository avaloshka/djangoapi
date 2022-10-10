from django.shortcuts import render
from .models import Course
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import CourseSerializer


# # Create your views here.
# def index(request):
# 	return render(request, 'index.html', {})

class CourseView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
