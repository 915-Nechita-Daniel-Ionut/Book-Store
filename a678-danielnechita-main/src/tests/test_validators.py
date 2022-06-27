from src.domain.book_entity import Book
from src.domain.client_entity import Client
from src.domain.rental_entity import Rental

from src.validators.book_validator import BookValidator
from src.validators.client_validator import ClientValidator
from src.validators.rental_validator import RentalValidator
from src.validators.validator_exception import ValidatorException

import unittest


class TestBookValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_book_negative_id = Book(-1, "author1", "title1")
        self.test_book_empty_author = Book(1, "", "title1")
        self.test_book_empty_title = Book(1, "author1", "")

    def test_book_validator__receive_negative_id__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, BookValidator.validate, self.test_book_negative_id)

    def test_book_validator__receive_empty_author__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, BookValidator.validate, self.test_book_empty_author)

    def test_book_validator__receive_empty_title__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, BookValidator.validate, self.test_book_empty_title)


class TestClientValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_client_negative_id = Client(-1, "name1")
        self.test_client_empty_name = Client(12, "")

    def test_client_validator__receive_negative_id__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, ClientValidator.validate, self.test_client_negative_id)

    def test_client_validator__receive_empty_name__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, ClientValidator.validate, self.test_client_empty_name)


class TestRentalValidator(unittest.TestCase):
    def setUp(self) -> None:
        self.test_rental_negative_id = Rental(-1, 11, 111, "01.01.2021", "11.01.2021")
        self.test_rental_empty_rented_date = Rental(1, 11, 111, "", "11.01.2021")
        self.test_rental_empty_returned_date = Rental(1, 11, 111, "01.01.2021", "")

    def test_rental_validator__receive_negative_id__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, RentalValidator.validate, self.test_rental_negative_id)

    def test_rental_validator__receive_empty_rented_date__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, RentalValidator.validate, self.test_rental_empty_rented_date)

    def test_rental_validator__receive_empty_returned_date__expect__to_throw_ValidatorException(self):
        self.assertRaises(ValidatorException, RentalValidator.validate, self.test_rental_empty_returned_date)


if __name__ == "main":
    unittest.main()
