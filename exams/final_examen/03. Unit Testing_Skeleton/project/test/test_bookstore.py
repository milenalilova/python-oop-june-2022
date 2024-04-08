from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(20)

    def test_bookstore_init(self):
        book_limit = 50
        bookstore = Bookstore(book_limit)

        self.assertEqual(book_limit, bookstore.books_limit)
        self.assertEqual(bookstore.total_sold_books, 0)

    def test_raises_when_invalid_book_limit(self):
        with self.assertRaises(ValueError) as context:
            self.invalid_bookstore = Bookstore(0)
        self.assertEqual(str(context.exception), "Books limit of 0 is not valid")

    def test_receive_book_raises_when_limit_reached(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("It", 25)
        self.assertEqual(str(error.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_adds_proper_count(self):
        result = self.bookstore.receive_book("It", 10)

        self.assertEqual(len(self.bookstore), 10)
        self.assertEqual(result, "10 copies of It are available in the bookstore.")

    def test_receive_book_returns_new_availability(self):
        result = self.bookstore.receive_book("It", 5)

        self.assertEqual(len(self.bookstore), 5)
        self.assertEqual(result, "5 copies of It are available in the bookstore.")

        new_result = self.bookstore.receive_book("It", 10)

        self.assertEqual(len(self.bookstore), 15)
        self.assertEqual(new_result, "15 copies of It are available in the bookstore.")

    def test_sell_books_raises_when_book_doesnt_exists(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("It", 5)
        self.assertEqual(str(error.exception), "Book It doesn't exist!")

    def test_sell_books_raises_when_not_enough_books(self):
        result = self.bookstore.receive_book("It", 3)

        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("It", 5)
        self.assertEqual(str(error.exception), "It has not enough copies to sell. Left: 3")

    def test_sell_books_sells_proper_count(self):
        self.bookstore.receive_book("It", 10)

        result = self.bookstore.sell_book("It", 5)
        self.assertEqual(len(self.bookstore), 5)
        self.assertEqual(result, "Sold 5 copies of It")
        self.assertEqual(self.bookstore.total_sold_books, 5)
        result_second = self.bookstore.sell_book("It", 5)
        self.assertEqual(len(self.bookstore), 0)
        self.assertEqual(result_second, "Sold 5 copies of It")
        self.assertEqual(self.bookstore.total_sold_books, 10)

    def test_str_returns_proper_result(self):
        self.bookstore.receive_book("It", 5)
        self.bookstore.sell_book("It", 2)

        self.assertEqual(str(self.bookstore), "Total sold books: 2\n"
                                              "Current availability: 3\n"
                                              " - It: 3 copies")


if __name__ == '__main__':
    main()
