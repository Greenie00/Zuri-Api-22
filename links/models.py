from multiprocessing import AuthenticationError
from django.db import models

# Create your models here.
class Links(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=False)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
