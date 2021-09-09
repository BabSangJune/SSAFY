from django.db import models

# 함수 호출 이렇게 가능
# def articles_imgge_path(instance, filename):
#     return f'user_{instance.user.pk}'/{filename}

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #날짜 경로 가능
    image = models.ImageField(upload_to='images/', blank=True,)

    def __str__(self):
        return self.title
