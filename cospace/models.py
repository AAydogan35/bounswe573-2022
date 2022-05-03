from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import models as tinymce_models

# Create your models here.
class Post(models.Model):
    body = tinymce_models.HTMLField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)