
import copy


class BookRepository(object):
    """ The repository of books. Here is where the books are stored"""
    def __init__(self):
        self.__books = {}

    def __len__(self):
        return len(self.__books)

    def find_by_id(self, book_id):
        """ Function for finding a books by its id"""
        if book_id in self.__books:
            return self.__books[book_id]
        return None

    def get_author(self, book_id):
        """ Functionality for returning the author of a book"""
        return self.__books[book_id].author

    def get_title(self, book_id):
        """ Functionality for returning the title of a book"""
        return self.__books[book_id].title

    def save_book(self, book):
        """ Function for saving a book in the repository"""
        self.__books[book.book_id] = book

    def update(self, book_id_to_update, book_update):
        """ Function for updating a book"""
        for book_id in self.__books:
            if book_id_to_update == book_id:
                self.__books[book_id] = book_update

    def delete_book_by_id(self, book_id_to_delete):
        """ Function for deleting a book from the repository"""
        book_list_copy = copy.deepcopy(self.__books)
        for book_id in book_list_copy:
            if book_id_to_delete == book_id:
                del self.__books[book_id]

    def get_all_books(self):
        """ Function for getting the list of books"""
        return self.__books
