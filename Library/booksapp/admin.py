from django.contrib import admin
from .models import BookModel, AuthorModel
# Register your models here.


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publication_year', 'isbn', 'price']

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name', 'address']