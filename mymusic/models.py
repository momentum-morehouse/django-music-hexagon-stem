from django.db import models

# Create your models here.

class Album(models.Model):
  artist_name = models.CharField(max_lenth=255)
  title = models.CharField(max_length=255)
  date_released = models.DateField(null=True, blank=True)

  def __str__(self):
    return f'(self.name)'
