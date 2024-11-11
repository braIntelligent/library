from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_books, name='search'),
    path('description/<str:book_id>', views.descripcion, name='description')
]