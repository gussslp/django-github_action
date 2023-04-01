from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author  = models.CharField(max_length=50)
    comments = models.IntegerField(max_length=7)
    likes = models.IntegerField(max_length=7)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

class Video(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    comments = models.IntegerField(max_length=7)
    likes = models.IntegerField(max_length=7)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"

class Audio(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    time = models.CharField(max_length=10)
    comments = models.IntegerField(max_length=7)
    likes = models.IntegerField(max_length=7)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "audio"
        verbose_name_plural = "audios"