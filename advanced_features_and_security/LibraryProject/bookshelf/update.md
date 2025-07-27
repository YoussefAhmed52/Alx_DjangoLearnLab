from bookshelf.models import Book

# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Check the update
print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)