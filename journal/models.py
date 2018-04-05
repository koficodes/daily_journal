from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
class Journal(models.Model):
    title = models.CharField("Journal Title", max_length=200)
    content = models.TextField()
    published_on = models.DateField(default=date.today) #using current day as default

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show-journal', kwargs={'pk': self.pk})

