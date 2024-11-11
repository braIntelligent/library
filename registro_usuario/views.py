from django.shortcuts import render, redirect
from registro_usuario.services.consumo_api import *

def find_books(request):
    if request.method == 'POST':
        valor_input = request.POST.get('input-value')
        books = consumo_api_nombre(valor_input)
        if valor_input:
            return render(request, 'listado_libros.html',{'books': books, 'valor_input': valor_input})
    return render(request, 'buscador.html')

def descripcion(request, book_id):
    book = consumo_api_id(book_id)
    book["volumeInfo"]["authors"] = ", ".join(book["volumeInfo"]["authors"])
    return render(request, 'descripcion_libros.html', {'book': book})







