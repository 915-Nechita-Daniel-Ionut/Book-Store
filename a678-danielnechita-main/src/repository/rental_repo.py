import copy


class RentalRepository(object):
    """ This is the repository of rents"""
    def __init__(self):
        self.__rents = {}

    def __len__(self):
        return len(self.__rents)

    def find_by_id(self, rental_id):
        """ Function for finding a books by its id"""
        if rental_id in self.__rents:
            return self.__rents[rental_id]
        return None

    def book_id_getter(self, rental_id):
        return self.__rents[rental_id].book_id

    def client_id_getter(self, rental_id):
        return self.__rents[rental_id].client_id

    def rented_date_getter(self, rental_id):
        return self.__rents[rental_id].rented_date

    def returned_date_getter(self, rental_id):
        return self.__rents[rental_id].returned_date

    def save_rent(self, rental):
        """ Function for saving a rent in the repository"""
        self.__rents[rental.rental_id] = rental

    def get_all_rents(self):
        """ Function for getting the list of rents"""
        return self.__rents

    def update(self, rental_id_to_update, rent_update):
        """ Function for updating the returned date of a rent"""
        for rental_id in self.__rents:
            if rental_id_to_update == rental_id:
                self.__rents[rental_id] = rent_update

    def update_rented_date(self, rental_id_to_update, update_returned_date):
        rental = self.__rents[rental_id_to_update]
        rental.returned_date = update_returned_date
        self.update(rental_id_to_update, rental)

    def delete_rental_by_id(self, rental_id_to_delete):
        rental_list_copy = copy.deepcopy(self.__rents)
        for rental_id in rental_list_copy:
            if rental_id == rental_id_to_delete:
                del self.__rents[rental_id]