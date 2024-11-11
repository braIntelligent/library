from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_books, name='search'),
    path('books-list/', views.books_list, name='bookslist'),
    path('description/<str:book_id>', views.description, name='description')
]

handler404 = 'mi_app.views.custom_404'
