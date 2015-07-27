from django.shortcuts import render
from django.http import HttpResponse
import json

from api.models import Course
from rest_framework import viewsets
from api.serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer