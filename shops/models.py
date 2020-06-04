from django.db import models
from datetime import datetime
from agents.models import Agent

# Create your models here.


class Shop(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    size = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.size
