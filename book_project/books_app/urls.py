from django.urls import path 
from .views import *

urlpatterns =[
    path('books/',get_books,name='get_books'),
    path('book/<int:id>/',get_book,name='get_book'),
    path('create_book/',create_book,name='create_book'),
    path('update_book/<int:id>/',update_book,name='update_book'),
    path('delete_book/<int:id>/',delete_book,name='delete_book'),
    path('books_by_author/<str:author>/',get_books_by_author,name='get_books_by_author'),

]