from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)