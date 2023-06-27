from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from shelves.forms import BookSearchForm, BookForm
from shelves.models import Author, Genre, Book, Publication


def index(request):
    num_authors = Author.objects.count()
    num_books = Book.objects.count()
    num_genres = Genre.objects.count()
    num_publication = Publication.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_authors": num_authors,
        "num_books": num_books,
        "num_genres": num_genres,
        "num_publication": num_publication,
        "num_visits": num_visits + 1,
    }

    return render(request, "shelves/index.html", context=context)


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    fields = "__all__"
    success_url = reverse_lazy("shelves:author-list")


class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    fields = "__all__"
    success_url = reverse_lazy("shelves:author-list")


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy("")


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "shelves/book_list.html"
    queryset = Book.objects.all()
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)

        title = self.request.GET.get("title", "")

        context["search_form"] = BookSearchForm(initial=title)

        return context

    def get_queryset(self):
        title = self.request.GET.get("title")

        if title:
            return self.queryset.filter(username__icontains=title)

        return self.queryset


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("shelves:book-list")
    template_name = "shelves/book_form.html"


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("shelves:book-list")
    template_name = "shelves/book_form.html"


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    success_url = reverse_lazy("")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    paginate_by = 3


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("shelves:genre-list")
    template_name = "shelves/genre_form.html"


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("shelves:genre-list")
    template_name = "shelves/genre_form.html"


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("")


class PublicationListView(LoginRequiredMixin, generic.ListView):
    model = Publication
    paginate_by = 3


class PublicationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Publication
    fields = "__all__"
    success_url = reverse_lazy("shelves:publication-list")
    template_name = "shelves/publication_form.html"


class PublicationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Publication
    fields = "__all__"
    success_url = reverse_lazy("shelves:publication-list")
    template_name = "shelves/publication_form.html"


class PublicationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Publication
    success_url = reverse_lazy("")
