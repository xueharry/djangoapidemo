from api.models import Course
from rest_framework import serializers

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'course_id')
        