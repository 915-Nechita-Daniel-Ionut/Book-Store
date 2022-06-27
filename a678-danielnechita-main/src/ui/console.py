from src.validators.validator_exception import ValidatorException
from src.domain.exception_classes import *
import datetime



class Console:
    def __init__(self, book_services, client_services, rental_services, statistics_services, undo_redo_services):
        self.__book_services = book_services
        self.__client_services = client_services
        self.__rental_services = rental_services
        self.__statistics_service = statistics_services
        self.__undo_redo_services = undo_redo_services


################################################## BOOKS ###########################################################

    @staticmethod
    def print_book_services():
        print("1 - Add a book \n"
              "2 - Remove a book \n"
              "3 - Update a book \n"
              "4 - List the books \n"
              "5 - Search for books \n"
              "x - Go Back \n")

    @staticmethod
    def print_book_search_parameters():
        print("1 - Search by id \n"
              "2 - Search by author \n"
              "3 - Search by title \n")


    def ui_print_books(self):
        book_list = self.__book_services.book_list_getter()
        for book_id in book_list:
            book = book_list[book_id]
            print(book)

    @staticmethod
    def ui_print_searched_books(book_list):
        for book_list_index in range(len(book_list)):
            book = book_list[book_list_index]
            print(book)


    def book_option_1_add(self):
        try:
            id = input("Insert book id: ")
            if id.isnumeric():
                id = int(id)
            else:
                raise IdIsNotNumericException
            author = input("Insert author name: ")
            title = input("Insert book title: ")
            try:
                self.__book_services.add_book(id, author, title)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("delete_book", id))
            except ValidatorException as ve:
                print(ve)
        except IdIsNotNumericException:
            print("Id must be an integer")
        except IdAlreadyExistsException:
            print("Id already exists")

    def book_option_2_delete(self):
        try:
            book_id = input("Insert the id of the book: ")
            if book_id.isnumeric():
                book_id = int(book_id)
            else:
                raise IdIsNotNumericException
            try:
                author_and_title = self.__book_services.author_and_title_getter(book_id)
                author = author_and_title[0]
                title = author_and_title[1]
                self.__book_services.remove_book(book_id)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("add_book", book_id, author, title))
            except IdNotFoundException:
                print("Id not found")
        except IdIsNotNumericException:
            print("Id must be an integer")

    def book_option_3_update(self):
        try:
            id_to_update = input("Insert the id of the book you want to edit: ")
            if id_to_update.isnumeric():
                id_to_update = int(id_to_update)
            else:
                raise IdIsNotNumericException
            author_update = input("Insert the new author: ")
            title_update = input("Insert the new title: ")
            try:
                author_and_title = self.__book_services.author_and_title_getter(id_to_update)
                author = author_and_title[0]
                title = author_and_title[1]
                self.__book_services.book_update(id_to_update, author_update, title_update)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("restore_book", id_to_update, author, title))
            except ValidatorException as ve:
                print(ve)
        except IdIsNotNumericException:
            print("Id must be an integer")
        except IdNotFoundException:
            print("Id not found")

    def book_option_4_print(self):
        self.ui_print_books()

    def book_option_5_search(self):
        self.print_book_search_parameters()
        search_option = input("Select search option: ")
        search_parameter = input("Insert the parameter: ")
        try:
            if search_option.isnumeric():
                search_option = int(search_option)
            else:
                raise OptionValueException
            if search_option > 3 or search_option < 1:
                raise OptionIndexException
            if search_option == 1:
                book_list = self.__book_services.search_book_by_id(search_parameter)
                if len(book_list) > 0:
                    self.ui_print_searched_books(book_list)
                else:
                    print("No books found")
            elif search_option == 2:
                book_list = self.__book_services.search_book_by_author(search_parameter)
                if len(book_list) > 0:
                    self.ui_print_searched_books(book_list)
                else:
                    print("No books found")
            elif search_option == 3:
                book_list = self.__book_services.search_book_by_title(search_parameter)
                if len(book_list) > 0:
                    self.ui_print_searched_books(book_list)
                else:
                    print("No books found")

        except OptionValueException:
            print("The option must be an integer")
        except OptionIndexException:
            print("The option must be between 1 and 3")
        except IdIsNotNumericException:
            print("The id must be an integer")


    def book_menu(self):
        while True:
            self.print_book_services()
            book_option = input("Give your option: ")
            if book_option == 'x':
                break
            try:
                if book_option.isnumeric():
                    book_option = int(book_option)
                else:
                    raise OptionValueException
                if book_option > 5 or book_option < 1:
                    raise OptionIndexException
                if book_option == 1:
                    self.book_option_1_add()

                elif book_option == 2:
                    self.book_option_2_delete()

                elif book_option == 3:
                    self.book_option_3_update()

                elif book_option == 4:
                    self.book_option_4_print()

                elif book_option == 5:
                    self.book_option_5_search()

            except OptionValueException:
                print("The option has to be a number")
            except OptionIndexException:
                print("Option has to be between 1 and 5")

###################################################### CLIENTS ##################################################

    @staticmethod
    def print_client_services():
        print("1 - Add a client \n"
              "2 - Remove a client \n"
              "3 - Update a client \n"
              "4 - List the clients \n"
              "5 - Search for clients \n"
              "x - Go Back \n")

    @staticmethod
    def print_client_search_parameters():
        print("1 - Search by id \n"
              "2 - Search by name \n")

    @staticmethod
    def ui_print_searched_clients(client_list):
        for client_list_index in range(len(client_list)):
            client = client_list[client_list_index]
            print(client)

    def ui_print_clients(self):
        client_list = self.__client_services.client_list_getter()
        for client_id in client_list:
            client = client_list[client_id]
            print(client)

    def client_option_1_add(self):
        try:
            client_id = input("Insert client id: ")
            if client_id.isnumeric():
                client_id = int(client_id)
            else:
                raise IdIsNotNumericException
            client_name = input("Insert client name: ")
            try:
                self.__client_services.add_client(client_id, client_name)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("delete_client", client_id))
            except ValidatorException as ve:
                print(ve)
        except IdIsNotNumericException:
            print("Id must be an integer")
        except IdAlreadyExistsException:
            print("Id already exists")

    def client_option_2_delete(self):
        try:
            client_id = input("Insert the id of the client: ")
            if client_id.isnumeric():
                client_id = int(client_id)
            else:
                raise IdIsNotNumericException
            try:
                client_name = self.__client_services.client_name_getter(client_id)
                self.__client_services.remove_client(client_id)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("add_client", client_id, client_name))
            except IdNotFoundException:
                print("Id not found")
        except IdIsNotNumericException:
            print("Id must be an integer")


    def client_option_3_update(self):
        try:
            client_id_to_update = input("Insert the id of the client you want to edit: ")
            if client_id_to_update.isnumeric():
                client_id_to_update = int(client_id_to_update)
            else:
                raise IdIsNotNumericException
            name_update = input("Insert the new name: ")
            try:
                client_name = self.__client_services.client_name_getter(client_id_to_update)
                self.__client_services.client_update(client_id_to_update, name_update)
                self.__undo_redo_services.clear_redo_stack()
                self.__undo_redo_services.undo_stack.append(("restore_client", client_id_to_update, client_name))
            except ValidatorException as ve:
                print(ve)
        except IdIsNotNumericException:
            print("Id must be an integer")
        except IdNotFoundException:
            print("Id not found")


    def client_option_4_print(self):
        self.ui_print_clients()

    def client_option_5_search(self):
        self.print_client_search_parameters()
        search_option = input("Select search option: ")
        search_parameter = input("Insert the parameter: ")
        try:
            if search_option.isnumeric():
                search_option = int(search_option)
            else:
                raise OptionValueException
            if search_option > 2 or search_option < 1:
                raise OptionIndexException
            if search_option == 1:
                client_list = self.__client_services.search_client_by_id(search_parameter)
                if len(client_list) > 0:
                    self.ui_print_searched_clients(client_list)
                else:
                    print("No client found")
            elif search_option == 2:
                client_list = self.__client_services.search_client_by_name(search_parameter)
                if len(client_list) > 0:
                    self.ui_print_searched_clients(client_list)
                else:
                    print("No client found")

        except OptionValueException:
            print("The option must be an integer")
        except OptionIndexException:
            print("The option must be between 1 and 2")
        except IdIsNotNumericException:
            print("The id must be an integer")


    def client_menu(self):
        while True:
            self.print_client_services()
            client_option = input("Give your option: ")
            if client_option == 'x':
                break
            try:
                if client_option.isnumeric():
                    client_option = int(client_option)
                else:
                    raise OptionValueException

                if client_option > 5 or client_option < 1:
                    raise OptionIndexException

                if client_option == 1:
                    self.client_option_1_add()

                elif client_option == 2:
                    self.client_option_2_delete()

                elif client_option == 3:
                    self.client_option_3_update()

                elif client_option == 4:
                    self.client_option_4_print()

                elif client_option == 5:
                    self.client_option_5_search()

            except OptionValueException:
                print('The option has to be a number')
            except OptionIndexException:
                print("Option has to be between 1 and 5")

####################################################### RENTALS ######################################################

    @staticmethod
    def print_rental_services():
        print("1 - Rent a book \n"
              "2 - Return a book \n"
              "3 - Print the book rental history \n"
              "4 - Check if a book is available \n"
              "x - Go Back \n")

    def ui_print_rents(self):
        rent_list = self.__rental_services.rent_list_getter()
        for rental_id in rent_list:
            rental = rent_list[rental_id]
            print(rental)

    def rental_option_1_rent(self):
        try:
            rental_id = input("Insert rental id: ")
            book_id = input("Insert book id: ")
            client_id = input("Insert client id: ")
            if rental_id.isnumeric() and book_id.isnumeric() and client_id.isnumeric():
                rental_id = int(rental_id)
                book_id = int(book_id)
                client_id = int(client_id)
            else:
                raise IdIsNotNumericException

            returned_date = 'N/A'
            rented_date = input("Insert the rent day: ")
            tokens = rented_date.split(".", maxsplit=3)
            if len(tokens) != 3:
                raise InvalidDateException
            day = tokens[0]
            month = tokens[1]
            year = tokens[2]
            if day.isnumeric() and month.isnumeric() and year.isnumeric():
                isValidDate = True
                try:
                    datetime.datetime(int(year), int(month), int(day))
                except ValueError:
                    isValidDate = False

                if isValidDate:
                    try:
                        self.__rental_services.add_a_rent(rental_id, book_id, client_id, rented_date, returned_date)
                        self.__undo_redo_services.clear_redo_stack()
                        self.__undo_redo_services.undo_stack.append(("delete_rent", rental_id))
                    except ValidatorException as ve:
                        print(ve)
                else:
                    print("Invalid date")
            else:
                raise InvalidDateException
        except IdIsNotNumericException:
            print("IDs have to be integers")
        except IdAlreadyExistsException:
            print("Rental id already exists")
        except InvalidDateException:
            print("Invalid date")
        except BookNotAvailableException:
            print('Book not available')
        except IdNotFoundException:
            print("Book ID not found or client ID not found")

    def rental_option_2_return(self):
        try:
            book_id = input("Insert book id: ")
            if book_id.isnumeric():
                book_id = int(book_id)
            else:
                raise IdIsNotNumericException
            print("Date format: dd.mm.yyyy")
            returned_date = input("Insert return date: ")
            tokens = returned_date.split(".", maxsplit=3)
            if len(tokens) != 3:
                raise InvalidDateException
            returned_day = tokens[0]
            returned_month = tokens[1]
            returned_year = tokens[2]
            if returned_day.isnumeric() and returned_month.isnumeric() and returned_year.isnumeric():
                isValidDate = True
                try:
                    datetime.datetime(int(returned_year), int(returned_month), int(returned_day))
                except ValueError:
                    isValidDate = False

                if isValidDate:
                    rental_id_where_book_was_returned = self.__rental_services.add_a_return(book_id, returned_date)
                    self.__undo_redo_services.clear_redo_stack()
                    self.__undo_redo_services.undo_stack.append(("restore_rent", rental_id_where_book_was_returned))
                else:
                    print("Invalid date")
        except IdIsNotNumericException:
            print("Id is not numeric")
        except IdNotFoundException:
            print("Id not found")

    def rental_option_3_print(self):
        self.ui_print_rents()

    def rental_option_4_availability(self):
        try:
            book_id = input("Insert book id: ")
            if book_id.isnumeric():
                book_id = int(book_id)
            else:
                raise IdIsNotNumericException
            if self.__rental_services.available_book_check(book_id):
                print("Book is available")
            else:
                print("Book is not available")
        except IdIsNotNumericException:
            print("Id must be an integer")
        except IdNotFoundException:
            print("Id not found")


    def rental_menu(self):
        while True:
            self.print_rental_services()
            rental_option = input("Give your option: ")
            if rental_option == 'x':
                break
            try:
                if rental_option.isnumeric():
                    rental_option = int(rental_option)
                else:
                    raise OptionValueException
                if rental_option > 4 or rental_option < 1:
                    raise OptionIndexException

                if rental_option == 1:
                    self.rental_option_1_rent()

                elif rental_option == 2:
                    self.rental_option_2_return()

                elif rental_option == 3:
                    self.rental_option_3_print()

                elif rental_option == 4:
                    self.rental_option_4_availability()

            except OptionValueException:
                print("The option has to be a number")
            except OptionIndexException:
                print("Option has to be between 1 and 4")

################################################## STATISTICS #########################################################

    @staticmethod
    def print_statistics_services():
        print("1 - Print most rented books \n"
              "2 - Print most active clients \n"
              "3 - Print most rented author \n"
              "x - Go Back \n")

    def statistics_option_1_most_rented_books(self):
        rental_list_sorted = self.__statistics_service.sort_by_most_rented_books()
        for book in rental_list_sorted:
            id_of_book = book[0]
            times_rented = str(book[1])
            author_and_title = self.__book_services.author_and_title_getter(id_of_book)
            author = author_and_title[0]
            title = author_and_title[1]
            print(title + " by " + author + " rented " + times_rented + " times ")

    def statistics_option_2_most_active_clients(self):
        client_activity_list = self.__statistics_service.sort_by_most_active_clients()
        for client in client_activity_list:
            id_of_client = client[0]
            active_days = str(client[1])
            client_name = self.__client_services.client_name_getter(id_of_client)
            print(client_name + " active for " + active_days + " days")


    def statistics_option_3_most_rented_author(self):
        most_rented_author_list = self.__statistics_service.sort_by_most_rented_author()
        for author in most_rented_author_list:
            author_name = author[0]
            times_rented = str(author[1])
            print("Books written by " + author_name + " were rented " + times_rented + " times")

    def statistics_menu(self):
        while True:
            self.print_statistics_services()
            statistics_option = input("Give your option: ")

            if statistics_option == 'x':
                break

            try:
                if statistics_option.isnumeric():
                    statistics_option = int(statistics_option)
                else:
                    raise OptionValueException
                if statistics_option > 3 or statistics_option < 1:
                    raise OptionIndexException

                if statistics_option == 1:
                    self.statistics_option_1_most_rented_books()

                elif statistics_option == 2:
                    self.statistics_option_2_most_active_clients()

                elif statistics_option == 3:
                    self.statistics_option_3_most_rented_author()

            except OptionValueException:
                print("The value has to be a number")
            except OptionIndexException:
                print("Option has to be between 1 and 3")




#################################################### CONSOLE ##########################################################

    @staticmethod
    def print_menu_options():
        print("1 - Show book services \n"
              "2 - Show client services\n"
              "3 - Show rental services \n"
              "4 - Show statistics services \n"
              "5 - Undo \n"
              "6 - Redo \n"
              "x - Exit \n")

    def initialize_program(self):
        self.__book_services.add_book(6680, 'author0', 'title0')
        self.__book_services.add_book(6681, 'author1', 'title1')
        self.__book_services.add_book(6682, 'author2', 'title2')
        self.__book_services.add_book(6683, 'author2', 'title3')
        self.__book_services.add_book(6684, 'author4', 'title4')
        self.__book_services.add_book(6685, 'author5', 'title5')
        self.__book_services.add_book(6686, 'author6', 'title6')
        self.__book_services.add_book(6687, 'author5', 'title7')
        self.__book_services.add_book(6688, 'author8', 'title8')
        self.__book_services.add_book(6689, 'author9', 'title9')
        self.__book_services.add_book(16680, 'author103', 'tit_le10')
        self.__book_services.add_book(16681, 'author11', 'tit_le11')
        self.__book_services.add_book(16682, 'author1233', 'tit_le12')
        self.__book_services.add_book(16683, 'author124', 'tit_le13')
        self.__book_services.add_book(16684, 'author145', 'title14')
        self.__book_services.add_book(16685, 'author151', 'title15')
        self.__book_services.add_book(16686, 'aut_hor166', 'title16')
        self.__book_services.add_book(16687, 'aut_hor152', 'title17')
        self.__book_services.add_book(16688, 'aut_hor18', 'title18')
        self.__book_services.add_book(16689, 'aut_hor19', 'title19')
        self.__client_services.add_client(1000, 'client0')
        self.__client_services.add_client(1001, 'client1')
        self.__client_services.add_client(1002, 'client2')
        self.__client_services.add_client(1003, 'client3')
        self.__client_services.add_client(1004, 'client4')
        self.__client_services.add_client(1005, 'client5')
        self.__client_services.add_client(1006, 'client6')
        self.__client_services.add_client(1007, 'client7')
        self.__client_services.add_client(1008, 'client8')
        self.__client_services.add_client(1009, 'client9')
        self.__client_services.add_client(11000, 'client10')
        self.__client_services.add_client(11001, 'client11')
        self.__client_services.add_client(11002, 'client12')
        self.__client_services.add_client(11003, 'client13')
        self.__client_services.add_client(11004, 'client14')
        self.__client_services.add_client(11005, 'client15')
        self.__client_services.add_client(11006, 'cl_ient16')
        self.__client_services.add_client(11007, 'cl_ient17')
        self.__client_services.add_client(11008, 'cl_ient18')
        self.__client_services.add_client(11009, 'cl_ient19')
        self.__rental_services.add_a_rent(660, 6683, 1002, '15.11.2021', '18.11.2021')
        self.__rental_services.add_a_rent(661, 6683, 1003, '19.11.2021', 'N/A')
        self.__rental_services.add_a_rent(662, 6681, 1002, '17.10.2021', 'N/A')
        self.__rental_services.add_a_rent(663, 6682, 1005, '07.11.2021', '10.11.2021')
        self.__rental_services.add_a_rent(664, 6688, 1005, '09.10.2021', '13.11.2021')
        self.__rental_services.add_a_rent(665, 6682, 1006, '16.11.2021', 'N/A')
        self.__rental_services.add_a_rent(666, 6687, 1001, '04.08.2021', '18.11.2021')
        self.__rental_services.add_a_rent(667, 6689, 1007, '13.09.2021', '18.11.2021')
        self.__rental_services.add_a_rent(668, 6687, 1009, '19.11.2021', 'N/A')
        self.__rental_services.add_a_rent(669, 6684, 1007, '02.11.2021', '18.11.2021')
        self.__rental_services.add_a_rent(1660, 16680, 11002, '15.11.2021', 'N/A')
        self.__rental_services.add_a_rent(1661, 16681, 11003, '19.11.2021', 'N/A')
        self.__rental_services.add_a_rent(1662, 16682, 11002, '17.10.2021', 'N/A')
        self.__rental_services.add_a_rent(1663, 16683, 11005, '07.11.2021', 'N/A')
        self.__rental_services.add_a_rent(1664, 16684, 11005, '09.10.2021', 'N/A')
        self.__rental_services.add_a_rent(1665, 16685, 11006, '16.11.2021', 'N/A')
        self.__rental_services.add_a_rent(1666, 16686, 11001, '04.08.2021', 'N/A')
        self.__rental_services.add_a_rent(1667, 16687, 11007, '13.09.2021', 'N/A')
        self.__rental_services.add_a_rent(1668, 16688, 11009, '19.11.2021', 'N/A')
        self.__rental_services.add_a_rent(1669, 16689, 11007, '02.11.2021', 'N/A')

    def undo_command(self):
        self.__undo_redo_services.undo_function()

    def redo_command(self):
        self.__undo_redo_services.redo_function()

    def run_console(self):
        self.initialize_program()

        while True:
            self.print_menu_options()
            menu_option = input("Give your option: ")

            if menu_option == 'x':
                break

            try:
                if menu_option.isnumeric():
                    menu_option = int(menu_option)
                else:
                    raise OptionValueException
                if menu_option > 6 or menu_option < 1:
                    raise OptionIndexException

                if menu_option == 1:
                    self.book_menu()

                elif menu_option == 2:
                    self.client_menu()

                elif menu_option == 3:
                    self.rental_menu()

                elif menu_option == 4:
                    self.statistics_menu()

                elif menu_option == 5:
                    self.undo_command()

                elif menu_option == 6:
                    self.redo_command()

            except OptionValueException:
                print("The value has to be a number")
            except OptionIndexException:
                print("Option has to be between 1 and 6")
