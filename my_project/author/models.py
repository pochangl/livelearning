from __future__ import unicode_literals

from django.db import models

# Create your models here.

SEX_CHOICES = (
    ("F", "Female"),
    ("M", "Male")
)


class Author(models.Model):
    # id = models.PositiveInteger(primary_key=True)
    name = models.CharField("author_name", max_length=16, primary_key = True)
    birth_time = models.DateTimeField(null=True, default=None)
    birth_date = models.DateField(null=True, default=None)
    age = models.PositiveIntegerField(default=0)
    bio = models.TextField(blank=True, default="")
    sex = models.CharField(max_length=16, choices = SEX_CHOICES)
    # books

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="books") # foreign key author references author_author(name)
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

class OneToOneBook(models.Model):
    author = models.OneToOneField(Author, related_name="one_to_one_book")


class ManyToManyBook(models.Model):
    title = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author, related_name="many_to_many_book")

    def __str__(self):
        return "M2M: %s" % self.title


class DetailedBook(Book):
    # models.foreignKeyField(Book)
    year = models.PositiveIntegerField()


