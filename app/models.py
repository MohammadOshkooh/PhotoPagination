from django.db import models


class Photo(models.Model):
    photo = models.ImageField(upload_to='photo/')
    # Another fields
