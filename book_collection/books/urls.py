from django.urls import path
from .views import list_books, book_detail, add_book, edit_book, delete_book

urlpatterns = [
    path('', list_books, name='list_books'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]
