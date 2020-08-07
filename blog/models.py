from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title