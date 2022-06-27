
class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def rental_id(self):
        return self.__rental_id

    @rental_id.setter
    def rental_id(self, id_value):
        self.__rental_id = id_value

    @property
    def book_id(self):
        return self.__book_id

    @book_id.setter
    def book_id(self, id_value):
        self.__book_id = id_value

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, id_value):
        self.__client_id = id_value

    @property
    def rented_date(self):
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, date):
        self.__rented_date = date

    @property
    def returned_date(self):
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, date):
        self.__returned_date = date

    def __str__(self):
        return "RentalID:% s ,BookID:% s ,ClientID:% s ,RentDate:% s ,ReturnDate:% s" % (self.rental_id, self.book_id, self.client_id, self.rented_date, self.returned_date)




