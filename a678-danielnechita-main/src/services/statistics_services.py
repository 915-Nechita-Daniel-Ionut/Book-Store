import datetime

from datetime import date



class StatisticsService:
    def __init__(self, book_repo, client_repo, rental_repo):
        self.__book_repo = book_repo
        self.__client_repo = client_repo
        self.__rental_repo = rental_repo

    @staticmethod
    def days_between(date1, date2):
        return (date2 - date1).days

    def sort_by_most_rented_books(self):
        rental_list = self.__rental_repo.get_all_rents()
        book_frequency_dictionary = {}
        for rent_id in rental_list:
            rental_from_list = rental_list[rent_id]
            if rental_from_list.book_id in book_frequency_dictionary:
                book_frequency_dictionary[rental_from_list.book_id] = book_frequency_dictionary[rental_from_list.book_id] + 1
            else:
                book_frequency_dictionary[rental_from_list.book_id] = 1
        sorted_rental_list = [(book_id, book_frequency_dictionary[book_id]) for book_id in sorted(book_frequency_dictionary, key=book_frequency_dictionary.get, reverse=True)]
        return sorted_rental_list

    @staticmethod
    def convert_client_date_from_string_to_date(string_client_date):
        tokens = string_client_date.split(".", maxsplit=3)
        client_day = int(tokens[0])
        client_month = int(tokens[1])
        client_year = int(tokens[2])
        client_date = date(client_year, client_month, client_day)
        return client_date

    def sort_by_most_active_clients(self):
        today_date = date.today()
        rental_list = self.__rental_repo.get_all_rents()
        client_activity_dictionary = {}
        for rent_id in rental_list:
            rental_from_list = rental_list[rent_id]
            client_rent_date = rental_from_list.rented_date
            client_rent_date = self.convert_client_date_from_string_to_date(client_rent_date)

            if rental_from_list.returned_date != 'N/A':
                client_return_date = rental_from_list.returned_date
                client_return_date = self.convert_client_date_from_string_to_date(client_return_date)
            else:
                client_return_date = today_date
            days_of_rental = self.days_between(client_rent_date, client_return_date)

            if rental_from_list.client_id in client_activity_dictionary:
                client_activity_dictionary[rental_from_list.client_id] = client_activity_dictionary[rental_from_list.client_id] + days_of_rental
            else:
                client_activity_dictionary[rental_from_list.client_id] = days_of_rental

        sorted_activity_list = [(client_id, client_activity_dictionary[client_id]) for client_id in sorted(client_activity_dictionary, key=client_activity_dictionary.get, reverse=True)]
        return sorted_activity_list

    def sort_by_most_rented_author(self):
        rental_list = self.__rental_repo.get_all_rents()
        author_frequency_dictionary = {}
        for rent_id in rental_list:
            rental_from_list = rental_list[rent_id]
            book_id = rental_from_list.book_id
            author = self.__book_repo.get_author(book_id)
            if author in author_frequency_dictionary:
                author_frequency_dictionary[author] = author_frequency_dictionary[author] + 1
            else:
                author_frequency_dictionary[author] = 1

        sorted_author_list = [(author, author_frequency_dictionary[author]) for author in sorted(author_frequency_dictionary, key=author_frequency_dictionary.get, reverse=True)]
        return sorted_author_list











