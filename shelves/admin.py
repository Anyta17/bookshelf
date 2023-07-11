from django.contrib import admin

from shelves.models import Publication, Genre, Author, Book

admin.site.register(Publication)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
