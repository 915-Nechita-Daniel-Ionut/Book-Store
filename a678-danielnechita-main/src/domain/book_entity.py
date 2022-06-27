
class Book:
    def __init__(self, book_id, author, title):
        self.__book_id = book_id
        self.__author = author
        self.__title = title

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id_value):
        self.__book_id = book_id_value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, name):
        self.__author = name

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, name):
        self.__title = name

    def __str__(self):
        return "ID:% s ,Author:% s ,Title:% s" % (self.book_id, self.author, self.title)
