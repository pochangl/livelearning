from django.contrib import admin

from . import models
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class AuthorAdmin(ModelAdmin):
    list_display = ("name", "birth_time", "birth_date", "age", "bio", "sex")

class BookAdmin(ModelAdmin):
    list_display = ("id", "author", "title")


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.OneToOneBook)
admin.site.register(models.ManyToManyBook)
admin.site.register(models.DetailedBook)