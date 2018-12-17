from django.db import models
from django.core.files import File
# Create your models here.

class Book(models.Model):
    CATEGORY=(
        ('T', 'TEXTONLY'),
        ('A', 'AUDIO'),
        ('B', 'TEXTBOOK'),
    )
    book_title = models.CharField(max_length=200)
    book_category = models.CharField(max_length=2, choices=CATEGORY)
    book_img = models.FileField(upload_to='cover', null=True)
    book_pdf = models.FileField(upload_to='pdf', null=True)
    
    def __str__(self):
        return self.book_title


class MyPDF(models.Model):
    my_origin = models.ForeignKey(Book, on_delete=models.CASCADE)
    my_pdf = models.FileField(upload_to="rps",null=True)
    my_img = models.FileField(upload_to="my", null=True)
    my_name = models.CharField(max_length=100)
    my_start = models.IntegerField(default=1)
    my_end = models.IntegerField(default=10)

    def __str__(self):
        return self.my_name

    def save(self, path, *args, **kwargs):
        f = open(path,'rb')
        self.my_pdf.save(self.my_name+".pdf", File(f), save=False)
        f.close()
        super(MyPDF,self).save(*args,**kwargs)
    