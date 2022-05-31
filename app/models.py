from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Entry(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"entry : {self.name} | {self.author}"


class Blog(models.Model):
    name = models.CharField(max_length=20)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)

    def __str__(self):
        return f"blog : {self.name} | {self.entry}"
