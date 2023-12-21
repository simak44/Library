from django import forms
from .models import BookModel, AuthorModel


# This form is for BookModel
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = "__all__"
        labels = {'title':'Title', 'author':'Author', 'publication_year':'Publication Year',
                  'isbn':'ISBN', 'price':'Price'}


    

# This form is for AuthorModel
class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = "__all__"
        labels = {'first_name':'First Name', 'last_name':'Last Name', 'address':'Address'}
    