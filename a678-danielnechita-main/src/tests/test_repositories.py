from src.domain.book_entity import Book
from src.domain.client_entity import Client
from src.domain.rental_entity import Rental

from src.repository.book_repo import BookRepository
from src.repository.client_repo import ClientRepository
from src.repository.rental_repo import RentalRepository

import unittest


class TestBookRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.book_repo = BookRepository()
        self.test_book1 = Book(1, "author1", "title1")
        self.test_book2 = Book(2, "author2", "title2")
        self.book_repo.save_book(self.test_book1)


    def test_save_book__add_one_book_in_the_repository__expect_repository_length_to_increase_by_one(self):
        self.assertEqual(len(self.book_repo), 1)

    def test_find_by_id__add_one_book_in_the_repository__expect_to_find_the_book_in_the_repository_by_id(self):
        self.assertEqual(self.book_repo.find_by_id(1), self.test_book1)

    def test_get_author__return_the_author_of_a_saved_book__expect_to_return_the_author_of_the_book(self):
        self.assertEqual(self.book_repo.get_author(1), "author1")

    def test_get_title__return_the_title_of_a_saved_book__expect_to_return_the_title_of_the_book(self):
        self.assertEqual(self.book_repo.get_title(1), "title1")

    def test_update__update_the_author_and_the_title_of_an_Existing_book__title_and_author_are_updated(self):
        self.test_book_update = Book(1, "author1.1", "title1.1")
        self.book_repo.update(1, self.test_book_update)
        self.assertEqual(self.book_repo.find_by_id(1), self.test_book_update)

    def test_delete_book_by_id__delete_book_from_repository_by_id__expect_find_by_id_function_to_return_None(self):
        self.book_repo.delete_book_by_id(1)
        self.assertIsNone(self.book_repo.find_by_id(1))

    def test_get_all_books__return_the_books_in_from_the_repo__expect_all_books_to_be_returned(self):
        self.book_repo.save_book(self.test_book2)
        self.assertEqual(self.book_repo.get_all_books(), {self.test_book1.book_id: self.test_book1, self.test_book2.book_id: self.test_book2})


class TestClientRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.client_repo = ClientRepository()
        self.test_client1 = Client(1, "name1")
        self.test_client2 = Client(2, "name2")
        self.client_repo.save_client(self.test_client1)

    def test_save_client__add_one_client_in_the_repository__expect_repository_length_to_increase_by_1(self):
        self.assertEqual(len(self.client_repo), 1)

    def test_find_by_id__add_one_client_in_the_repository__expect_to_find_by_id_the_book_in_the_repository(self):
        self.assertEqual(self.client_repo.find_by_id(1), self.test_client1)

    def test_name_getter__return_the_name_of_a_client__expect_name_to_be_returned(self):
        self.assertEqual(self.client_repo.name_getter(1), "name1")

    def test_update__update_the_name_of_a_client__expect_name_to_be_updated(self):
        self.test_client_update = Client(1, "name1.1")
        self.client_repo.update(1, self.test_client_update)
        self.assertEqual(self.client_repo.find_by_id(1), self.test_client_update)

    def test_delete_client_by_id__delete_a_client_by_id__expect_find_by_id_function_to_return_None(self):
        self.client_repo.delete_client_by_id(1)
        self.assertIsNone(self.client_repo.find_by_id(1))

    def test_get_all_clients__get_the_clients_from_the_repository__expect_all_the_clients_to_be_returned(self):
        self.client_repo.save_client(self.test_client2)
        self.assertEqual(self.client_repo.get_all_clients(), {self.test_client1.client_id: self.test_client1, self.test_client2.client_id: self.test_client2})


class TestRentalRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.rental_repo = RentalRepository()
        self.test_rental1 = Rental(1, 11, 111, "01.01.2021", "N/A")
        self.test_rental2 = Rental(2, 22, 222, "02.02.2021", "N/A")
        self.rental_repo.save_rent(self.test_rental1)

    def test_save_rent__add_a_rental_to_the_repository__expect_repository_length_to_increase_by_1(self):
        self.assertEqual(len(self.rental_repo), 1)

    def test_find_by_id__find_book_in_the_repository_by_id__expect_to_find_the_book_in_the_repository(self):
        self.assertEqual(self.rental_repo.find_by_id(1), self.test_rental1)

    def test_book_id_getter__get_the_book_id_from_a_rental__expect_book_id_to_be_returned(self):
        self.assertEqual(self.rental_repo.book_id_getter(1), 11)

    def test_client_id_getter__get_the_client_id_from_a_rental__expect_client_id_to_be_returned(self):
        self.assertEqual(self.rental_repo.client_id_getter(1), 111)

    def test_rented_date_getter__get_the_rented_date_from_a_rental__expect_rented_date_to_be_returned(self):
        self.assertEqual(self.rental_repo.rented_date_getter(1), "01.01.2021")

    def test_returned_date_getter__get_the_returned_date_from_a_rental__expect_returned_date_to_be_returned(self):
        self.assertEqual(self.rental_repo.returned_date_getter(1), "N/A")

    def test_get_all_rents__get_the_rents_from_the_repository__expect_to_get_all_the_rents_in_the_repository(self):
        self.rental_repo.save_rent(self.test_rental2)
        self.assertEqual(self.rental_repo.get_all_rents(), {self.test_rental1.rental_id: self.test_rental1, self.test_rental2.rental_id: self.test_rental2})

    def test_update__update_a_rental_from_the_repository__expect_rental_to_be_updated(self):
        self.test_rental_update = Rental(1, 12, 123, "01.01.2021", "11.01.2021")
        self.rental_repo.update(1, self.test_rental_update)
        self.assertEqual(self.rental_repo.find_by_id(1), self.test_rental_update)

    def test_delete_rental_by_id__delete_a_rental_from_the_repository_by_id__expect_find_by_id_function_to_return_None(self):
        self.rental_repo.delete_rental_by_id(1)
        self.assertIsNone(self.rental_repo.find_by_id(1))



if __name__ == "main":
    unittest.main()

