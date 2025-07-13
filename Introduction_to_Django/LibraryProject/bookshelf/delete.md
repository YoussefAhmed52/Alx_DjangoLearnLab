from bookshelf.models import Book

# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check that the book is deleted
print(Book.objects.all())
# Output: <QuerySet []>