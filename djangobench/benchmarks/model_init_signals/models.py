from django.db import models
from django.db.models.signals import pre_init, post_init

class Book(models.Model):
    title = models.CharField(max_length=100)

class AnotherModel(models.Model):
    pass

def handler(*args, **kwargs):
    pass

pre_init.connect(handler, sender=AnotherModel)
post_init.connect(handler, sender=AnotherModel)
