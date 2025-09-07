from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import books
# Create your views here.
def products(request):
    book = books.objects.all()
    return render(request, 'products/products.html', {'books': book})

def product(request, pk):
    book = get_object_or_404(books, pk=pk)
    return render(request, 'products/product.html', {'book': book})