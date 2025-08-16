from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')
        
        # Create author and book
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(
            title='Book One',
            publication_year=2020,
            author=self.author
        )
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.list_url = reverse('book-list')

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_book_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        data = {
            "title": "Updated Title",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + '?title=Book One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_author(self):
        response = self.client.get(self.list_url + '?search=Author One')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        Book.objects.create(title='Second Book', publication_year=2018, author=self.author)
        response = self.client.get(self.list_url + '?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data[0]['publication_year'] <= response.data[1]['publication_year'])

    def test_unauthenticated_create_fails(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
