from django.shortcuts import render
from .models import Books
# Create your views here.

uploaded_books = Books.objects.all()

context = {
    'books':uploaded_books
}


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def books(request):
    return render(request, 'books.html', context)