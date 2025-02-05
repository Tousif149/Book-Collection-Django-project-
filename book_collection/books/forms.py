from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'summary']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise forms.ValidationError("A book with this title already exists.")
        return title
