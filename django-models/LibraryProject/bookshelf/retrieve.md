from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Year: {book.publication_year}")
# Output: Title: 1984, Author: George Orwell, Year: 1949