from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homepage, name = "home"),
    path("books/", books, name='books'),
    path("add-book/", add_book, name = "add-book"),
    path("del-book/<id>/", del_book, name="del-book"),
    path("mark-book/<id>/", mark_book, name="mark-book"),
    path("unmark-book/<id>/", unmark_book, name="unmark-book"),
    path("book/<id>/", BooksDetail, name="book"),
]   + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
