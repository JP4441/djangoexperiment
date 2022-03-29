from django.db import models
from django.urls import reverse

# Create your models here.


class Finch(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  image = models.CharField(default = None, blank= True, null = True, max_length=2000)


## redirecting user to details after uploading new finch profile
  def get_absolute_url(self):
      return reverse('detail', kwargs={'finch_id': self.id})