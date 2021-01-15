from django.db import models
from django.conf import settings

class Post(models.Model) :
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)
    price=models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}>{self.name}'

