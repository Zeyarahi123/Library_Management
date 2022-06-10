from django import forms
from .models import BooksModel
from .models import RegisterModel
# creating a forms
class BooksForm(forms.ModelForm):
    #create meta class
    class Meta:
        model=BooksModel

        fields=[
            "Book_Name",
            "Author_Name",
            "Title",
            "Desc_Book",
            "Book_Price"
        ]

class RegisterForm(forms.ModelForm):
        # create meta class
        class Meta:
            model = RegisterModel

            fields = [
                "name",
                "email",
                "username",
                "password"

            ]