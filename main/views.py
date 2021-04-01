from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BookShop

def homepage(request):
    return render(request, "index.html")

def books(request):
    books_list = BookShop.objects.all()
    return render(request, "books.html", {"books_list": books_list})

def add_book(request):
    form = request.POST
    title = form["b_title"]
    subtitle = form["b_subtitle"]
    author = form["b_author"]
    price = form["b_price"]
    genre = form["b_genre"]
    description = form["b_description"]
    year = form["b_year"]
    book = BookShop(
        title=title, 
        subtitle = subtitle, 
        author=author, 
        price=price, 
        genre=genre, 
        description=description, 
        year=year
    )
    book.save()
    return redirect(books)

def del_book(request, id):
    b = BookShop.objects.get(id=id)
    b.delete()
    return redirect(books)

def mark_book(request, id):
    b = BookShop.objects.get(id=id)
    b.is_favorites = True
    b.save()
    return redirect(books)

def unmark_book(request, id):
    b = BookShop.objects.get(id=id)
    b.is_favorites = False
    b.save()
    return redirect(books)


def BooksDetail(request, id):
    book_d = BookShop.objects.get(id=id)
    return render(request, "book_detail.html", {"book_d": book_d})

