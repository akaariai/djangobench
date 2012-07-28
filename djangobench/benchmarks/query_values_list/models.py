from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    d1 = models.TextField(null=True)
    d2 = models.TextField(null=True)
    d3 = models.TextField(null=True)
    d4 = models.TextField(null=True)
    d5 = models.TextField(null=True)
    d6 = models.TextField(null=True)
