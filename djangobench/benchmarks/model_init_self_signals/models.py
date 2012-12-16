from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

def noop(*args, **kwargs):
    pass
models.signals.pre_init.connect(noop, sender=Book)
models.signals.post_init.connect(noop, sender=Book)
