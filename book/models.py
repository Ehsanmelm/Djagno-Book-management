from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class BooksModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    class Meta:
        db_table = 'books'

class ReviewsModel(models.Model):
    book = models.ForeignKey(BooksModel , on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5) , MinValueValidator(1)])

    class Meta:
        db_table = 'reviews'