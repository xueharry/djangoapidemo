from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)