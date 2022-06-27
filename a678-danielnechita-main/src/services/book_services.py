from src.domain.book_entity import Book
from src.domain.exception_classes import *


class BookService:
    """ This is a service class for books, storing them in a repository and adding/removing,
    updating and listing the books"""

    def __init__(self, book_repo, book_validator):
        self.__book_repo = book_repo
        self.__book_validator = book_validator

    def author_and_title_getter(self, book_id):
        try:
            author = self.__book_repo.get_author(book_id)
            title = self.__book_repo.get_title(book_id)
            return author, title
        except KeyError:
            raise IdNotFoundException

    def add_book(self, book_id, author, title):
        """ Function for adding a book"""
        book = Book(book_id, author, title)
        self.__book_validator.validate(book)
        if self.__book_repo.find_by_id(book_id) is None:
            self.__book_repo.save_book(book)
        else:
            raise IdAlreadyExistsException

    def book_list_getter(self):
        """ Function for getting the list of books"""
        book_list = self.__book_repo.get_all_books()
        return book_list

    def remove_book(self, book_id_to_delete):
        """ Function for removing a book from the list"""
        if self.__book_repo.find_by_id(book_id_to_delete) is not None:
            self.__book_repo.delete_book_by_id(book_id_to_delete)
        else:
            raise IdNotFoundException

    def book_update(self, book_id_to_update, author_update, title_update):
        """ Function for updating a book's author or title"""
        book = Book(book_id_to_update, author_update, title_update)
        self.__book_validator.validate(book)
        if self.__book_repo.find_by_id(book_id_to_update) is not None:
            self.__book_repo.update(book_id_to_update, book)
        else:
            raise IdNotFoundException

    def search_book_by_id(self, searched_id):
        if not searched_id.isnumeric():
            raise IdIsNotNumericException
        book_list = self.book_list_getter()
        search_book_list = []
        for book_id in book_list:
            book = book_list[book_id]
            if searched_id in str(book.book_id):
                search_book_list.append(book)
        return search_book_list

    def search_book_by_author(self, searched_author):
        book_list = self.book_list_getter()
        search_book_list = []
        for author in book_list:
            book = book_list[author]
            if searched_author.lower() in book.author.lower():
                search_book_list.append(book)
        return search_book_list

    def search_book_by_title(self, searched_title):
        book_list = self.book_list_getter()
        search_book_list = []
        for title in book_list:
            book = book_list[title]
            if searched_title.lower() in book.title.lower():
                search_book_list.append(book)
        return search_book_list
