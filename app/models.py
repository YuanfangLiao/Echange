# Create your models here.
from django.db import models
from django.db.models import DO_NOTHING

__all__ = ["Book", "Publisher", "Author"]


class Book(models.Model):
    title = models.CharField(max_length=32)
    CHOICE = ((1, "Python"), (2, "Linux"), (3, "go"))
    category = models.IntegerField(choices=CHOICE)
    pub_time = models.DateField()
    publisher = models.ForeignKey(to="Publisher", on_delete=DO_NOTHING)
    authors = models.ManyToManyField(to="Author")


class Publisher(models.Model):
    title = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)


class Good(models.Model):
    name = models.CharField(max_length=32)
