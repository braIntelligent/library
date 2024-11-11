from django.shortcuts import render
from registro_usuario.services.consumo_api import *
from django.http import HttpResponseRedirect
from django.urls import reverse

def find_books(request):
    if request.method == 'POST':
        valor_input = request.POST.get('input-value')
        url = reverse('bookslist') + f'?query={valor_input}'
        return HttpResponseRedirect(url)
    return render(request, 'search.html')

def books_list(request):
    valor_input = request.GET.get('query')
    if valor_input:
        print('valorinput', valor_input)
        books = consumo_api_nombre(valor_input)
        return render(request, 'books_list.html',{'books': books, 'valor_input': valor_input})
    return render(request, 'search.html')

def description(request, book_id):
    valor_input = request.GET.get('query') 
    book = consumo_api_id(book_id)
    book["volumeInfo"]["authors"] = ", ".join(book["volumeInfo"]["authors"])
    return render(request, 'books_description.html', {'book': book, 'valor_input': valor_input})

def custom_404(request, exception):
    return render(request, '404.html', status=404)




