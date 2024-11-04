from django.db import models

# Create your models here.

class Weblog(models.Model):
    weblog = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.weblog