from django.contrib import admin
from .models import BooksModel , ReviewsModel

# Register your models here.

admin.site.register(BooksModel)
admin.site.register(ReviewsModel)