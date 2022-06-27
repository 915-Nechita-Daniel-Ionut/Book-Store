
from src.domain.rental_entity import Rental
from src.domain.exception_classes import *


class RentalService:
    """This is a service class for tracking every rent that happens in the Library"""
    def __init__(self, rental_repo, book_repo, client_repo, rental_validator):
        self.__rental_repo = rental_repo
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_validator = rental_validator

    def rent_list_getter(self):
        """Function for getting the list of rents"""
        rent_list = self.__rental_repo.get_all_rents()
        return rent_list

    def available_book_check(self, book_id):
        """Function for getting the list of available books"""
        if self.__book_repo.find_by_id(book_id) is not None:
            rents_list = self.__rental_repo.get_all_rents()
            book_availability_check = True
            for rent_id in rents_list:
                rental_from_list = rents_list[rent_id]
                if rental_from_list.book_id == book_id:
                    if rental_from_list.returned_date == 'N/A':
                        book_availability_check = False
            return book_availability_check
        else:
            raise IdNotFoundException


    def add_a_rent(self, rental_id, book_id, client_id, rented_date, returned_date):
        """ Function for adding a rent to the list"""
        if self.__book_repo.find_by_id(book_id) is not None and self.__client_repo.find_by_id(client_id) is not None:
            book_availability_check = self.available_book_check(book_id)
            if book_availability_check:
                rental = Rental(rental_id, book_id, client_id, rented_date, returned_date)
                self.__rental_validator.validate(rental)
                if self.__rental_repo.find_by_id(rental_id) is None:
                    self.__rental_repo.save_rent(rental)
                else:
                    raise IdAlreadyExistsException
            else:
                raise BookNotAvailableException
        else:
            raise IdNotFoundException


    def add_a_return(self, book_id, returned_date):
        """Function for updating the rent. The returned date is updated from N/A to the date when the book is returned"""
        if self.__book_repo.find_by_id(book_id) is not None:
            rental_list = self.__rental_repo.get_all_rents()
            for rental_id in rental_list:
                rent = rental_list[rental_id]
                if rent.book_id == book_id and rent.returned_date == 'N/A':
                    client_id = rent.client_id
                    rented_date = rent.rented_date
                    rent_update = Rental(rental_id, book_id, client_id, rented_date, returned_date)
                    self.__rental_repo.update(rental_id, rent_update)
                    return rental_id
        else:
            raise IdNotFoundException

    def delete_a_rent(self, rental_id):
        self.__rental_repo.delete_rental_by_id(rental_id)

    def restore_rent_returned_date(self, rental_id, update_returned_date):
        self.__rental_repo.update_rented_date(rental_id, update_returned_date)

    def book_id__client_id__rent_date__returned_date_getter(self, rental_id):
        book_id = self.__rental_repo.book_id_getter(rental_id)
        client_id = self.__rental_repo.client_id_getter(rental_id)
        rented_date = self.__rental_repo.rented_date_getter(rental_id)
        returned_date = self.__rental_repo.returned_date_getter(rental_id)
        return book_id, client_id, rented_date, returned_date


