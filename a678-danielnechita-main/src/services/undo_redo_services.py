
class UndoRedoService:
    """ This is a service class for making and undo or redo operation of the previous command from user"""
    def __init__(self, book_services, client_services, rental_services):
        self.__book_services = book_services
        self.__client_services = client_services
        self.__rental_services = rental_services
        self.undo_stack = []
        self.redo_stack = []

    def undo_function(self):
        if len(self.undo_stack) > 0:
            last_operation = self.undo_stack.pop()
            command_word = last_operation[0]
            if command_word == "delete_book":  # anti add
                id_to_delete = last_operation[1]
                author_and_title = self.__book_services.author_and_title_getter(id_to_delete)
                author = author_and_title[0]
                title = author_and_title[1]
                self.redo_stack.append(("add_book", id_to_delete, author, title))
                self.__book_services.remove_book(id_to_delete)
            elif command_word == "add_book":  # anti delete
                book_id = last_operation[1]
                author = last_operation[2]
                title = last_operation[3]
                self.redo_stack.append(("delete_book", book_id))
                self.__book_services.add_book(book_id, author, title)
            elif command_word == "restore_book":  # anti update
                book_id = last_operation[1]
                author = last_operation[2]
                title = last_operation[3]
                author_and_title_redo = self.__book_services.author_and_title_getter(book_id)
                author_redo = author_and_title_redo[0]
                title_redo = author_and_title_redo[1]
                self.redo_stack.append(("update_book", book_id, author_redo, title_redo))
                self.__book_services.book_update(book_id, author, title)
            elif command_word == "delete_client":  # anti add
                id_to_delete = last_operation[1]
                client_name = self.__client_services.client_name_getter(id_to_delete)
                self.redo_stack.append(("add_client", id_to_delete, client_name))
                self.__client_services.remove_client(id_to_delete)
            elif command_word == "add_client":  # anti delete
                client_id = last_operation[1]
                client_name = last_operation[2]
                self.redo_stack.append(("delete_client", client_id))
                self.__client_services.add_client(client_id, client_name)
            elif command_word == "restore_client":  # anti update
                client_id = last_operation[1]
                client_name = last_operation[2]
                client_name_redo = self.__client_services.client_name_getter(client_id)
                self.redo_stack.append(("update_client", client_id, client_name_redo))
                self.__client_services.client_update(client_id, client_name)
            elif command_word == "delete_rent":  # anti add
                rental_id = last_operation[1]
                rental_parameters = self.__rental_services.book_id__client_id__rent_date__returned_date_getter(rental_id)
                book_id = rental_parameters[0]
                client_id = rental_parameters[1]
                rented_date = rental_parameters[2]
                returned_date = rental_parameters[3]
                self.redo_stack.append(("add_rent", rental_id, book_id, client_id, rented_date, returned_date))
                self.__rental_services.delete_a_rent(rental_id)
            elif command_word == "restore_rent":  # anti update
                rental_id = last_operation[1]
                rental_parameters = self.__rental_services.book_id__client_id__rent_date__returned_date_getter(rental_id)
                returned_date_redo = rental_parameters[3]
                self.redo_stack.append(("update_rent", rental_id, returned_date_redo))
                self.__rental_services.restore_rent_returned_date(rental_id, "N/A")


    def redo_function(self):
        if len(self.redo_stack) > 0:
            last_undo = self.redo_stack.pop()
            command_word = last_undo[0]
            if command_word == "add_book":
                book_id = last_undo[1]
                author = last_undo[2]
                title = last_undo[3]
                self.undo_stack.append(("delete_book", book_id))
                self.__book_services.add_book(book_id, author, title)
            elif command_word == "delete_book":
                book_id = last_undo[1]
                author_and_title = self.__book_services.author_and_title_getter(book_id)
                author = author_and_title[0]
                title = author_and_title[1]
                self.undo_stack.append(("add_book", author, title))
                self.__book_services.remove_book(book_id)
            elif command_word == "update_book":
                book_id = last_undo[1]
                author = last_undo[2]
                title = last_undo[3]
                author_and_title_undo = self.__book_services.author_and_title_getter(book_id)
                author_undo = author_and_title_undo[0]
                title_undo = author_and_title_undo[1]
                self.undo_stack.append(("restore_book", book_id, author_undo, title_undo))
                self.__book_services.book_update(book_id, author, title)
            elif command_word == "add_client":
                client_id = last_undo[1]
                client_name = last_undo[2]
                self.undo_stack.append(("delete_client", client_id))
                self.__client_services.add_client(client_id, client_name)
            elif command_word == "delete_client":
                client_id = last_undo[1]
                client_name = self.__client_services.client_name_getter(client_id)
                self.undo_stack.append(("add_client", client_name, client_id))
            elif command_word == "update_client":
                client_id = last_undo[1]
                client_name = last_undo[2]
                client_name_redo = self.__client_services.client_name_getter(client_id)
                self.undo_stack.append(("restore_client", client_id, client_name_redo))
                self.__client_services.client_update(client_id, client_name)
            elif command_word == "add_rent":
                rental_id = last_undo[1]
                book_id = last_undo[2]
                client_id = last_undo[3]
                rented_date = last_undo[4]
                returned_date = last_undo[5]
                self.undo_stack.append(("delete_rent", rental_id))
                self.__rental_services.add_a_rent(rental_id, book_id, client_id, rented_date, returned_date)
            elif command_word == "update_rent":
                rental_id = last_undo[1]
                returned_date = last_undo[2]
                self.undo_stack.append(("restore_rent", rental_id))
                self.__rental_services.restore_rent_returned_date(rental_id, returned_date)


    def clear_redo_stack(self):
        self.redo_stack.clear()

    def print_redo_stack(self):
        print(self.redo_stack)
