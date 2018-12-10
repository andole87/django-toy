from django.db import models
# Create your models here.

class Book(models.Model):
    CATEGORY=(
        ('T', 'TEXTONLY'),
        ('A', 'AUDIO'),
        ('B', 'TEXTBOOK'),
    )
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=30)
    book_price = models.DecimalField(decimal_places=10, max_digits=10)
    book_page_number = models.IntegerField(default=0)
    book_category = models.CharField(max_length=2, choices=CATEGORY)

    def __str__(self):
        return self.book_title

class BookDetail(models.Model):
    book_img = models.