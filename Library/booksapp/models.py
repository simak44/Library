from django.db import models

# Create your models here.

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # return self.first_name 
    # def __str__(self) :
    #     return self.last_name





class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE )
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length= 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 4)

    # def __str__(self):
    #     return self.title




