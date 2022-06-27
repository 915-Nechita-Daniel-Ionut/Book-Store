from src.domain.book_entity import Book
from src.domain.client_entity import Client
from src.domain.rental_entity import Rental

from src.repository.book_repo import BookRepository
from src.repository.client_repo import ClientRepository
from src.repository.rental_repo import RentalRepository

from src.services.book_services import BookService
from src.services.client_services import ClientService
from src.services.rental_services import RentalService
from src.services.statistics_services import StatisticsService
from src.services.undo_redo_services import UndoRedoService

from src.validators.book_validator import BookValidator
from src.validators.client_validator import ClientValidator
from src.validators.rental_validator import RentalValidator
from src.validators.validator_exception import ValidatorException

from src.domain.exception_classes import *


import unittest


class TestBookServices(unittest.TestCase):
    def setUp(self) -> None:
        self.book_repo = BookRepository()
        self.book_validator = BookValidator()
        self.book_services = BookService(self.book_repo, self.book_validator)
        self.book_services.add_book(1, "author1", "title1")

    def test_author_and_title_getter__receive_id_of_existent_book__return_the_author_and_the_title_of_the_book(self):
        self.assertEqual(self.book_services.author_and_title_getter(1), ("author1", "title1"))

    def test_add_book__add_one_book_in_the_repository__expect_repository_length_increased_by_1(self):
        self.assertEqual(len(self.book_repo), 1)

    def test_add_book__add_one_book_in_the_repository__expect_find_by_id_to_find_the_book(self):
        self.assertIsNotNone(self.book_repo.find_by_id(1))

    def test_remove_book__remove_book_having_given_id__expect_repository_length_decreased_by_1(self):
        self.book_services.remove_book(1)
        self.assertEqual(len(self.book_repo), 0)

    def test_remove_book__remove_book_having_given_id__expect_find_by_id_function_to_return_None(self):
        self.book_services.remove_book(1)
        self.assertIsNone(self.book_repo.find_by_id(1))

    def test_book_update__update_author_and_title_to_new_strings__book_is_updated_to_the_new_strings(self):
        self.book_services.book_update(1, "author1.1", "title1.1")
        self.assertEqual(self.book_services.author_and_title_getter(1), ("author1.1", "title1.1"))

    def test_search_book_by_author__search_for_books_where_author_partially_match_with_given_string__returns_list_with_found_books(self):
        self.book_services.add_book(2, "Bob Ross", "title2")
        self.assertEqual(self.book_services.search_book_by_author("auth"), [self.book_repo.find_by_id(1)])

    def test_search_book_by_title__search_for_books_where_title_partially_match_with_given_string__returns_list_with_found_books(self):
        self.book_services.add_book(2, "Bob Ross", "Bob")
        self.assertEqual(self.book_services.search_book_by_title("Bo"), [self.book_repo.find_by_id(2)])

    def test_search_book_by_id__search_for_books_where_id_partially_match_with_given_number__returns_list_with_found_books(self):
        self.book_services.add_book(223, "Bob Ross", "title2")
        self.assertEqual(self.book_services.search_book_by_id('223'), [self.book_repo.find_by_id(223)])


class TestClientServices(unittest.TestCase):
    def setUp(self) -> None:
        self.client_repo = ClientRepository()
        self.client_validator = ClientValidator()
        self.client_services = ClientService(self.client_repo, self.client_validator)
        self.client_services.add_client(1, "name1")

    def test_client_name_getter__receive_id_of_existing_client__returns_name_of_client(self):
        self.assertEqual(self.client_services.client_name_getter(1), "name1")

    def test_add_client__add_a_client_in_the_repository__expect_repository_length_increased_by_one(self):
        self.assertEqual(len(self.client_repo), 1)

    def test_remove_client__remove_client_from_repository__expect_repository_length_decreased_by_one(self):
        self.client_services.remove_client(1)
        self.assertEqual(len(self.client_repo), 0)

    def test_remove_client__remove_client_from_repository__expect_find_by_id_function_returns_None(self):
        self.client_services.remove_client(1)
        self.assertIsNone(self.client_repo.find_by_id(1))

    def test_client_update__update_name_of_client_to_new_string__client_name_updated_to_new_string(self):
        self.client_services.client_update(1, "name1.1")
        self.assertEqual(self.client_services.client_name_getter(1), "name1.1")

    def test_search_client_by_id__search_for_clients_where_id_partially_matches_with_given_number__return_list_of_found_clients(self):
        self.client_services.add_client(2, "Bob")
        self.assertEqual(self.client_services.search_client_by_id('1'), [self.client_repo.find_by_id(1)])

    def test_search_client_by_name__search_for_clients_where_name_partially_matches_with_given_string__return_list_of_found_clients(self):
        self.client_services.add_client(2, "Bob")
        self.assertEqual(self.client_services.search_client_by_name("bo"), [self.client_repo.find_by_id(2)])


class TestRentalServices(unittest.TestCase):
    def setUp(self) -> None:
        self.rental_repo = RentalRepository()
        self.rental_validator = RentalValidator()
        self.book_repo = BookRepository()
        self.book_validator = BookValidator()
        self.book_services = BookService(self.book_repo, self.book_validator)
        self.client_repo = ClientRepository()
        self.client_validator = ClientValidator()
        self.client_services = ClientService(self.client_repo, self.client_validator)
        self.rental_services = RentalService(self.rental_repo, self.book_repo, self.client_repo, self.rental_validator)
        self.book_services.add_book(11, "author1", "title1")
        self.book_services.add_book(22, "author2", "title2")
        self.client_services.add_client(111, "Bob")
        self.rental_services.add_a_rent(1, 11, 111, "01.01.2021", 'N/A')

    def test_available_book_check__check_if_book_is_available_for_rental__returns_True_or_False(self):
        self.assertFalse(self.rental_services.available_book_check(11))
        self.assertTrue(self.rental_services.available_book_check(22))

    def test_add_a_rent__add_a_rent_in_the_repository__expect_repository_length_increased_by_1(self):
        self.assertEqual(len(self.rental_repo), 1)

    def test_add_a_return__add_the_returned_date_of_a_rented_book__expect_returned_date_to_be_updated_from_not_available(self):
        self.rental_services.add_a_return(11, "03.12.2021")
        self.assertEqual(self.rental_repo.returned_date_getter(1), "03.12.2021")
        self.assertNotEqual(self.rental_repo.returned_date_getter(1), "N/A")

    def test_delete_a_rent__delete_a_rent_from_repository__repository_length_decreased_by_1(self):
        self.rental_services.delete_a_rent(1)
        self.assertEqual(len(self.rental_repo), 0)

    def test_delete_a_rent__delete_a_rent_from_repository__find_by_id_function_returns_None(self):
        self.rental_services.delete_a_rent(1)
        self.assertIsNone(self.rental_repo.find_by_id(1))

    def test_restore_rent_returned_date__restore_returned_date_to_not_available__returned_date_is_restored(self):
        self.rental_services.add_a_return(11, "03.12.2021")
        self.assertEqual(self.rental_repo.returned_date_getter(1), "03.12.2021")
        self.rental_services.restore_rent_returned_date(1, "N/A")
        self.assertEqual(self.rental_repo.returned_date_getter(1), "N/A")


class TestStatisticsService(unittest.TestCase):
    def setUp(self) -> None:
        self.rental_repo = RentalRepository()
        self.rental_validator = RentalValidator()
        self.book_repo = BookRepository()
        self.book_validator = BookValidator()
        self.book_services = BookService(self.book_repo, self.book_validator)
        self.client_repo = ClientRepository()
        self.client_validator = ClientValidator()
        self.client_services = ClientService(self.client_repo, self.client_validator)
        self.rental_services = RentalService(self.rental_repo, self.book_repo, self.client_repo, self.rental_validator)
        self.statistics_services = StatisticsService(self.book_repo, self.client_repo, self.rental_repo)
        self.book_services.add_book(11, "author1", "title1")
        self.book_services.add_book(22, "author2", "title2")
        self.client_services.add_client(111, "Bob")
        self.client_services.add_client(222, "Mark")
        self.rental_services.add_a_rent(1, 11, 111, "01.01.2021", "12.01.2021")
        self.rental_services.add_a_rent(2, 11, 222, "01.01.2021", 'N/A')
        self.rental_services.add_a_rent(3, 22, 111, "01.01.2021", 'N/A')

    def test_sort_by_most_rented_books__find_and_sort_the_rented_books_by_most_rented__return_list_of_found_books_sorted_by_most_rented(self):
        sorted_book_list = self.statistics_services.sort_by_most_rented_books()
        self.assertEqual(sorted_book_list[0], (11, 2))
        self.assertEqual(sorted_book_list[1], (22, 1))

    def test_sort_by_most_active_clients__find_and_sort_the_clients_by_most_active__return_list_of_found_clients_sorted_by_most_active(self):
        sorted_clients_list = self.statistics_services.sort_by_most_active_clients()
        self.assertEqual(sorted_clients_list[0], (111, 347))
        self.assertEqual(sorted_clients_list[1], (222, 336))

    def test_sort_by_most_rented_author__finds_and_sort_the_authors_by_most_books_rented__return_list_of_found_authors_sorted_by_most_books_rented(self):
        sorted_author_list = self.statistics_services.sort_by_most_rented_author()
        self.assertEqual(sorted_author_list[0], ("author1", 2))
        self.assertEqual(sorted_author_list[1], ("author2", 1))


class TestUndoRedoService(unittest.TestCase):
    def setUp(self) -> None:
        self.rental_repo = RentalRepository()
        self.rental_validator = RentalValidator()
        self.book_repo = BookRepository()
        self.book_validator = BookValidator()
        self.book_services = BookService(self.book_repo, self.book_validator)
        self.client_repo = ClientRepository()
        self.client_validator = ClientValidator()
        self.client_services = ClientService(self.client_repo, self.client_validator)
        self.rental_services = RentalService(self.rental_repo, self.book_repo, self.client_repo, self.rental_validator)
        self.statistics_services = StatisticsService(self.book_repo, self.client_repo, self.rental_repo)
        self.undo_redo_services = UndoRedoService(self.book_services, self.client_services, self.rental_services)

    def test_undo_function____add_a_book__check_if_added__call_undo____expect_find_by_id_of_book_to_return_None_after_undo_call(self):
        self.book_services.add_book(1, "author1", "title1")
        self.undo_redo_services.undo_stack.append(("delete_book", 1))
        self.assertIsNotNone(self.book_repo.find_by_id(1))
        self.undo_redo_services.undo_function()
        self.assertIsNone(self.book_repo.find_by_id(1))

    def test_redo_function____add_a_book__undo__check_if_undone__redo_last_undo____expect_find_by_id_function_to_find_the_book_after_redo_call(self):
        self.book_services.add_book(1, "author1", "title1")
        self.undo_redo_services.undo_stack.append(("delete_book", 1))
        self.assertIsNotNone(self.book_repo.find_by_id(1))
        self.undo_redo_services.undo_function()
        self.assertIsNone(self.book_repo.find_by_id(1))
        self.undo_redo_services.redo_function()
        self.assertIsNotNone(self.book_repo.find_by_id(1))


if __name__ == "main":
    unittest.main()

