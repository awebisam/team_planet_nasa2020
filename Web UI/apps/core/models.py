from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings


class Contact(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fname = models.CharField(max_length=75)
    lname = models.CharField(max_length=75)
    age = models.IntegerField()
    no_of_times = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Newsletter Email"
        verbose_name_plural = "Newsletter Emails"

    def __str__(self):
        return self.email
