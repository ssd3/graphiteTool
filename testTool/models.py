from django.db import models

# Create your models here.


class TestCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
