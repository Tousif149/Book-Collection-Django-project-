from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# List all books and support search
def list_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) if query else Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})

# Show details of a book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

# Add a new book
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})

# Edit an existing book
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form, "book": book})

# Delete a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, "books/delete_book.html", {"book": book})
