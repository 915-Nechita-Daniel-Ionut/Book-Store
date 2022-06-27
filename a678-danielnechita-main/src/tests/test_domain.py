from src.domain.book_entity import Book
from src.domain.client_entity import Client
from src.domain.rental_entity import Rental
import unittest


class TestBookEntity(unittest.TestCase):
    def setUp(self) -> None:
        self.test_book1 = Book(1, "author1", "title1")
        self.test_book2 = Book(2, "author2", "title2")

    def test_book_entity__create_a_book_object__expect_book_id_to_be_correct(self):
        self.assertEqual(self.test_book1.book_id, 1)
        self.assertEqual(self.test_book2.book_id, 2)

    def test_book_entity__test_book_entity__create_a_book_object__expect_title_to_be_correct(self):
        self.assertEqual(self.test_book1.title, "title1")
        self.assertEqual(self.test_book2.title, "title2")

    def test_book_entity__test_book_entity__create_a_book_object__expect_author_to_be_correct(self):
        self.assertEqual(self.test_book1.author, "author1")
        self.assertEqual(self.test_book2.author, "author2")

    def test_book_entity__check_if_book_author_can_be_changed__else_throw_AssertionError(self):
        self.test_book1.author = "author1.1"
        self.test_book2.author = "author2.1"
        self.assertEqual(self.test_book1.author, "author1.1")
        self.assertEqual(self.test_book2.author, "author2.1")

    def test_book_entity__check_if_book_title_can_be_changed__else_throw_AssertionError(self):
        self.test_book1.title = "title1.1"
        self.test_book2.title = "title2.1"
        self.assertEqual(self.test_book1.title, "title1.1")
        self.assertEqual(self.test_book2.title, "title2.1")

    def test_book_entity__check_if_book_can_be_printed__else_throw_AssertionError(self):
        self.assertEqual(str(self.test_book1), "ID:1 ,Author:author1 ,Title:title1")
        self.assertEqual(str(self.test_book2), "ID:2 ,Author:author2 ,Title:title2")


class TestClientEntity(unittest.TestCase):
    def setUp(self) -> None:
        self.test_client1 = Client(1, "name1")
        self.test_client2 = Client(2, "name2")

    def test_client_entity__check_if_client_id_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_client1.client_id, 1)
        self.assertEqual(self.test_client2.client_id, 2)

    def test_client_entity__check_if_client_name_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_client1.client_name, "name1")
        self.assertEqual(self.test_client2.client_name, "name2")

    def test_client_entity__check_if_client_name_can_be_changed__else_throw_AssertionError(self):
        self.test_client1.client_name = "name1.1"
        self.test_client2.client_name = "name2.1"
        self.assertEqual(self.test_client1.client_name, "name1.1")
        self.assertEqual(self.test_client2.client_name, "name2.1")

    def test_client_entity__check_if_client_can_be_printed__else_throw_AssertionError(self):
        self.assertEqual(str(self.test_client1), "ID:1 ,Name:name1")
        self.assertEqual(str(self.test_client2), "ID:2 ,Name:name2")


class TestRentalEntity(unittest.TestCase):
    def setUp(self) -> None:
        self.test_rental1 = Rental(1, 11, 111, "01.01.2021", "11.01.2021")
        self.test_rental2 = Rental(2, 22, 222, "02.02.2021", "22.01.2021")

    def test_rental_entity__check_if_rental_id_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_rental1.rental_id, 1)
        self.assertEqual(self.test_rental2.rental_id, 2)

    def test_rental_entity__check_if_book_id_of_rental_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_rental1.book_id, 11)
        self.assertEqual(self.test_rental2.book_id, 22)

    def test_rental_entity__check_if_client_id_of_rental_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_rental1.client_id, 111)
        self.assertEqual(self.test_rental2.client_id, 222)

    def test_rental_entity__check_if_rented_date_of_rental_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_rental1.rented_date, "01.01.2021")
        self.assertEqual(self.test_rental2.rented_date, "02.02.2021")

    def test_rental_entity__check_if_returned_date_of_rental_is_correct__else_throw_AssertionError(self):
        self.assertEqual(self.test_rental1.returned_date, "11.01.2021")
        self.assertEqual(self.test_rental2.returned_date, "22.01.2021")

    def test_rental_entity__check_if_rental_can_be_printed__else_throw_Assertion_error(self):
        self.assertEqual(str(self.test_rental1), "RentalID:1 ,BookID:11 ,ClientID:111 ,RentDate:01.01.2021 ,ReturnDate:11.01.2021")
        self.assertEqual(str(self.test_rental2), "RentalID:2 ,BookID:22 ,ClientID:222 ,RentDate:02.02.2021 ,ReturnDate:22.01.2021")

if __name__ == "main":
    unittest.main()

