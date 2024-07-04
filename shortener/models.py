from django.db import models


class Url(models.Model):
    url = models.TextField(max_length=150)
    shortened_url = models.TextField(unique=True, null=True)

    
    