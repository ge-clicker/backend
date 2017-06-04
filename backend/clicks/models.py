from django.db import models
from colorfield.fields import ColorField


class Party(models.Model):
    name = models.TextField()
    primary_color = ColorField()
    secondary_color = ColorField(null=True, blank=True)
    image = models.URLField()


class ClickRecord(models.Model):
    party = models.ForeignKey(Party, related_name='clicks')
    clicks = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    created_time = models.DateTimeField(auto_now_add=True)
