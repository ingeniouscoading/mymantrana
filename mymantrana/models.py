from django.db import models

# Create your models here.

class Books(models.Model):
    book_title = models.TextField(max_length=100, null=False)
    book_cover_front = models.FileField(upload_to='books', blank=False)
    book_cover_back = models.FileField(upload_to='books', blank=False)
    book_sample = models.FileField(upload_to='books', blank=False)
    book_author1 = models.TextField(max_length=50, null=False)
    book_author2 = models.TextField(max_length=50, null=True)
    book_publisher = models.TextField(max_length=100, null=True)
    buy_link1 = models.URLField(max_length=255)
    buy_link2 = models.URLField(max_length=255)
    date = models.DateField(auto_created=True)

    def __str__(self) -> str:
        return self.book_title