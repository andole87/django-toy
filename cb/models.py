from django.db import models

# Create your models here.

class BookMeta(models.Model):
    book_name = models.CharField(max_length=50,db_index=True)
    book_img = models.FileField(upload_to='cover', null=True)
    book_pdf = models.FileField(upload_to='pdf', null=True)
    is_text = models.BooleanField(db_index=True)

    def __str__(self):
        return self.book_name

class Usr(models.Model):
    GRADE=(
        ('A', 'Premium'),
        ('B', 'Regular'),
        ('C', 'Guest'),
    )
    usr_name = models.CharField(max_length=30)
    usr_pwd = models.CharField(max_length=30)
    usr_grade = models.CharField(choices=GRADE,max_length=2,db_index=True)

    def __str__(self):
        return self.usr_name

class Rps(models.Model):
    usr_id = models.ForeignKey(Usr, on_delete=models.CASCADE)
    rps_name = models.CharField(max_length=30)
    rps_pdf = models.FileField(upload_to='rps')

    def __str__(self):
        return self.rps_name

