import pytest
from datetime import date, timedelta
from .models import Author, Book, Offer

@pytest.mark.django_db
class TestModels:

    def test_author_creation(self):
        author = Author.objects.create(name="Ahmed", email="ahmed@example.com")
        assert author.name == "Ahmed"
        assert author.email == "ahmed@example.com"
        assert author.count == 0

    def test_book_creation(self):
        author = Author.objects.create(name="Laila", email="laila@example.com")
        book = Book.objects.create(
            title="Django Simplified",
            publication_date=date.today(),
            price=99.99,
            stock=10,
            author=author
        )
        assert book.title == "Django Simplified"
        assert book.author == author
        assert book.stock == 10

    def test_offer_creation(self):
        author = Author.objects.create(name="Sara", email="sara@example.com")
        book = Book.objects.create(
            title="Python Basics",
            publication_date=date.today(),
            price=49.99,
            stock=5,
            author=author
        )
        offer = Offer.objects.create(
            name="New Year Discount",
            discount=15.00,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=10),
            book=book
        )
        assert offer.book == book
        assert offer.discount == 15.00
