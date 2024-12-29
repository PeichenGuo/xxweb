from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    ]
    username = models.CharField(max_length=64, verbose_name="Username",unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    def __unicode__(self):
        return self.username
    def __str__(self):
        return self.username