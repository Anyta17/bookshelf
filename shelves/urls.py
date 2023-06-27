from django.urls import path

from shelves.views import (
    index,
    AuthorListView,
    AuthorDetailView,
    AuthorCreateView,
    AuthorDeleteView,
    AuthorUpdateView,
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    PublicationListView,
    PublicationCreateView,
    PublicationUpdateView,
    PublicationDeleteView,
    GenreListView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/create", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/delete", AuthorDeleteView.as_view(), name="author-delete"),
    path("authors/<int:pk>/update", AuthorUpdateView.as_view(), name="author-update"),

    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create", BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/delete", BookDeleteView.as_view(), name="book-delete"),
    path("books/<int:pk>/update", BookUpdateView.as_view(), name="book-update"),

    path("publications/", PublicationListView.as_view(), name="publication-list"),
    path("publications/create", PublicationCreateView.as_view(), name="publication-create"),
    path("publications/<int:pk>/delete", PublicationDeleteView.as_view(), name="publication-delete"),
    path("publications/<int:pk>/update", PublicationUpdateView.as_view(), name="publication-update"),

    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/create", GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/delete", GenreDeleteView.as_view(), name="genre-delete"),
    path("genres/<int:pk>/update", GenreUpdateView.as_view(), name="genre-update"),
]

app_name = "shelves"
