from django.db import models

# Create your models here.
class BooksModel(models.Model):
    Book_Name=models.CharField(max_length=200)
    Author_Name=models.CharField(max_length=200)
    Title=models.CharField(max_length=200)
    Desc_Book=models.TextField()
    Book_Price=models.IntegerField()


    def __str__(self):
        return self.Book_Name

class RegisterModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=40)

    def __str__(self):
        return self.email


