>>>from bookshelf.models import Book
>>> book=Book.objects.create(title="1984", author="George Orwell", publication_year="1949") 
>>> print(book)
1984
>>> from bookshelf.models import Book
>>> book=Book.objects.get(title="1984")
>>> print(book.title)
1984
>>> print(book.author)
George Orwell
>>> print(book.publication_year)
1949
>>> from bookshelf.models import Book   
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four
>>> from bookshelf.models import Book     
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all()) 
<QuerySet []>