from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Book(models.Model):
    title = models.CharField(max_length=100)

class AnotherModel(models.Model):
    im = models.ImageField(upload_to='foo')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
