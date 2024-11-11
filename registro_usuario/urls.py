from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_books, name='buscador'),
    path('descripcion/<str:book_id>', views.descripcion, name='descripcion')
]