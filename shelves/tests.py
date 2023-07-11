from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from shelves.models import Genre, Publication, Book


class AuthorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = get_user_model().objects.create_user(username="Jay Kristoff")

    def test_author_list_view(self):
        url = reverse("shelves:author-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_author_detail_view(self):
        url = reverse("shelves:author-detail", kwargs={"pk": self.author.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_author_create_view(self):
        url = reverse("shelves:author-create")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_author_delete_view(self):
        url = reverse("shelves:author-delete", kwargs={"pk": self.author.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_author_update_view(self):
        url = reverse("shelves:author-update", kwargs={"pk": self.author.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)


class BookTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.publication = Publication.objects.create(name="КСД")
        self.genre = Genre.objects.create(genre="fantasy")
        self.book = Book.objects.create(
            title="Shadow and Bone",
            publication=self.publication,
            genre=self.genre,
            price=220
        )

    def test_book_list_view(self):
        url = reverse('shelves:book-list')
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_book_detail_view(self):
        url = reverse('shelves:book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_book_create_view(self):
        url = reverse("shelves:book-create")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_book_delete_view(self):
        url = reverse("shelves:book-delete", kwargs={"pk": self.book.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_book_update_view(self):
        url = reverse("shelves:book-update", kwargs={"pk": self.book.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)


class GenreTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.genre = Genre.objects.create(genre="detective")

    def test_genre_list_view(self):
        url = reverse("shelves:genre-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_genre_create_view(self):
        url = reverse("shelves:genre-create")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_genre_delete_view(self):
        url = reverse("shelves:genre-delete", kwargs={"pk": self.genre.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_genre_update_view(self):
        url = reverse("shelves:genre-update", kwargs={"pk": self.genre.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)


class PublicationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.publication = Publication.objects.create(name="Vivat")

    def test_publication_list_view(self):
        url = reverse("shelves:publication-list")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_publication_create_view(self):
        url = reverse("shelves:publication-create")
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_publication_delete_view(self):
        url = reverse("shelves:publication-delete", kwargs={"pk": self.publication.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)

    def test_publication_update_view(self):
        url = reverse("shelves:publication-update", kwargs={"pk": self.publication.pk})
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)


class PublicFormatTests(TestCase):
    def test_genre_login_required(self):
        result = self.client.get(reverse("shelves:genre-list"))

        self.assertNotEqual(result.status_code, 200)

    def test_publication_login_required(self):
        result = self.client.get(reverse("shelves:publication-list"))

        self.assertNotEqual(result.status_code, 200)

    def test_book_login_required(self):
        result = self.client.get(reverse("shelves:book-list"))

        self.assertNotEqual(result.status_code, 200)


class PrivateFormatTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "12345678"
        )
        self.client.force_login(self.user)

    def test_retrieve_publication(self):
        Publication.objects.create(name="Bookchef")
        Publication.objects.create(name="Sky")

        response = self.client.get(reverse("shelves:publication-list"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "shelves/publication_list.html")

    def test_retrieve_book(self):
        vivat = Publication.objects.create(name="Vivat")
        bookchef = Publication.objects.create(name="Bookchef")
        fantasy = Genre.objects.create(genre="fantasy")
        Book.objects.create(
            title="Throne of glass",
            publication=vivat,
            genre=fantasy,
            price=350
        )
        Book.objects.create(
            title="From blood and ash",
            publication=bookchef,
            genre=fantasy,
            price=400
        )

        response = self.client.get(reverse("shelves:book-list"))
        book = Book.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["book_list"]),
            list(book)
        )
        self.assertTemplateUsed(response, "shelves/book_list.html")
