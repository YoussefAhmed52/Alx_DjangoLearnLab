from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"\n📚 Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name: {author_name}")

    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\n📚 Books in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name: {library_name}")

    try:
        librarian = Librarian.objects.get(library)
        print(f"\n👤 Librarian of {library_name}: {librarian.name}")
    except:
        print("Couldn't find the librarian for that library.")
