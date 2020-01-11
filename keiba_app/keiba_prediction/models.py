from django.db import models

# Create your models here.

class Horse(models.Model):
    horse = models.CharField(max_length=100)
    f_horse = models.CharField(max_length=100)
    m_horse = models.CharField(max_length=100)
    ff_horse = models.CharField(max_length=100)
    fm_horse = models.CharField(max_length=100)
    mf_horse = models.CharField(max_length=100)
    mm_horse = models.CharField(max_length=100)
    age = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) + str(self.horse)