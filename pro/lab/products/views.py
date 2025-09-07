from django.shortcuts import render, get_object_or_404
from .models import books

def products(request):
    action = request.GET.get('action')
    genre = request.GET.get('genre')
    q = request.GET.get('q')

    book_qs = books.objects.all()  
  

    if action == "fiction":
        book_qs = book_qs.filter(genre="Fiction")
    elif action == "expensive":
        book_qs = book_qs.order_by('-price')
    elif action == "available":
        book_qs = book_qs.exclude(stock=0)
    elif action == "exact":
        book_qs = book_qs.filter(name__exact="Django for Beginners")
    elif action == "in":
        book_qs = book_qs.filter(price__in=[23, 200, 500])
    elif action == "range":
        book_qs = book_qs.filter(price__range=(0, 3000))

    if genre:
        book_qs = book_qs.filter(genre=genre)

    if q:
        book_qs = book_qs.filter(name__icontains=q)

    return render(request, 'products/products.html', {'books': book_qs})


def product(request, pk):
    book = get_object_or_404(books, pk=pk)
    return render(request, 'products/product.html', {'book': book})
