from django.db import models
from django.urls import reverse
from django.conf import settings

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete = models.PROTECT)
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):

    def __str__(self):
        return self.text
    text = models.TextField(default='')
    list = models.ForeignKey(List, default = None, on_delete = models.PROTECT)
    
    class Meta:
        unique_together = ('list','text')
        ordering = ('id',)