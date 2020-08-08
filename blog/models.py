# from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField

# class Post(models.Model):
#     body = RichTextUploadingField(blank=True)

from django.db import models

from ckeditor.fields import RichTextField

class Post(models.Model):
    body = RichTextField(null=True, blank=True)

