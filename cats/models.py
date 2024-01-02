from random import choice
from django.db import models

class Cat(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.ImageField(upload_to='cat_images')

    @classmethod
    def get_random_cat(cls):
        ids = cls.objects.values_list('id', flat=True)
        cat = cls.objects.get(id=choice(ids))
        return cat
    class Meta:
        indexes = [
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']