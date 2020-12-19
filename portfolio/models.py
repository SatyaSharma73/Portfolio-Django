from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images', height_field=None, width_field=None, max_length=100, **options)
    url=models.URLField(blank=True)