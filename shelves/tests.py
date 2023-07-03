from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from shelves.models import Genre, Publication, Book


class ModelsTests(TestCase):
    def test_genre_str(self):
        genre = Genre.objects.create(
            genre="novel"
        )
        self.assertEqual(str(genre), genre.genre)

    def test_publication_str(self):
        publication = Publication.objects.create(name="Vivat")

        self.assertEqual(str(publication), publication.name)

    def test_book_str(self):
        genre = Genre.objects.create(genre="fantasy")
        pub_house = Publication.objects.create(name="Vivat")
        book = Book.objects.create(
            title="Nevernight",
            pub_house=pub_house,
            genre=genre,
            price=600)

        self.assertEqual(str(book),
                         f"{book.title}: {genre.genre}"
                         )


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
            pub_house=vivat,
            genre=fantasy,
            price=350
        )
        Book.objects.create(
            title="From blood and ash",
            pub_house=bookchef,
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
