from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
