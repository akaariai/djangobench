from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)

class Other(models.Model):
    pass

def noop(*args, **kwargs):
    pass
models.signals.pre_init.connect(noop, sender=Other)
models.signals.post_init.connect(noop, sender=Other)
