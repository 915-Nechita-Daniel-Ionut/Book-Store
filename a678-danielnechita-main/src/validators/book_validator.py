
from src.domain.book_entity import Book
from src.validators.validator_exception import ValidatorException


class BookValidator:
    @staticmethod
    def validate(book):
        errors = ""
        if isinstance(book, Book) is False:
            errors += "It is not a book! \n"
        if int(book.book_id) < 1:
            errors += "Id must be a positive integer \n"
        if book.title == "":
            errors += "Title can't be empty! \n"
        if book.author == "":
            errors += "Author can't be empty! \n"
        if errors != "":
            raise ValidatorException(errors)
