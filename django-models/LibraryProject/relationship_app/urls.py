from django.template import Library
from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    # Registration view (custom)
    path('register/', views.register, name='register'),  

    # Login view (built-in)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout view (built-in)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('books/', list_books, name='book-list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
]
