# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Data(models.Model):
    temperature = models.CharField(max_length=10, blank=True, default='')
    humidity = models.CharField(max_length=10, blank=True, default='')