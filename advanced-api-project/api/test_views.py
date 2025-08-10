from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.client.login(username="testuser", password="pass1234")

        # Create some books
        self.book1 = Book.objects.create(title="Book A", author="Author X", publication_year=2001)
        self.book2 = Book.objects.create(title="Book B", author="Author Y", publication_year=2005)

        # URLs
        self.list_url = reverse('book-list')  # from your urls.py name
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    def test_create_book(self):
        """Test creating a new book"""
        data = {'title': 'Book C', 'author': 'Author Z', 'publication_year': 2010}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating a book"""
        data = {'title': 'Book A Updated', 'author': 'Author X', 'publication_year': 2001}
        response = self.client.put(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Book A Updated')

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.list_url, {'author': 'Author X'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author X')

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url, {'search': 'Book A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book A')

    def test_order_books_by_year(self):
        """Test ordering books by publication_year"""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years))

    def test_unauthenticated_create_fails(self):
        """Test that unauthenticated users cannot create books"""
        self.client.logout()
        data = {'title': 'Book D', 'author': 'Author W', 'publication_year': 2020}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)