from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        ordering = ('user',)


class account_data(models.Model):
    username = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        unique_together = ("username", "key")
