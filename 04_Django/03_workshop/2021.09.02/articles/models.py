from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #조회수
    def __str__(self):
        return self.title