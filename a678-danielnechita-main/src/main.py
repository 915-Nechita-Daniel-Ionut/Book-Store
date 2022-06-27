from src.services.book_services import BookService
from src.services.client_services import ClientService
from src.services.rental_services import RentalService

from src.ui.console import Console

from src.repository.book_repo import BookRepository
from src.repository.client_repo import ClientRepository
from src.repository.rental_repo import RentalRepository

#from src.tests.test_book_service import TestBookService
#from src.tests.test_client_service import TestClientService

from src.validators.client_validator import ClientValidator
from src.validators.book_validator import BookValidator
from src.validators.rental_validator import RentalValidator

from src.services.statistics_services import StatisticsService
from src.services.undo_redo_services import UndoRedoService

"""
Assignment 06 - 08
Requirements
You will solve one of the problems below using simple feature-driven development
Your program must provide a menu-driven console-based user interface. Implementation details are up to you


For week 8 (25% of grade)
Implement features 1 and 2
Have at least 20 procedurally generated items in your application at startup
Provide specification and tests for all non-UI classes and methods for the first functionality
Implement and use your own exception classes.

For week 9 (25% of grade)
Implement features 3 and 4
Implement PyUnit test cases

For week 10 (50% of grade)
All features must be implemented
"""
"""4. Library
Write an application for a book library. The application will store:

Book: book_id, title, author
Client: client_id, name
Rental: rental_id, book_id, client_id, rented_date, returned_date
Create an application to:

1.Manage clients and books. The user can add, remove, update, and list both clients and books.

2.Rent or return a book. A client can rent an available book. A client can return a rented book at any time. 
Only available books (those which are not currently rented) can be rented.

3.Search for clients or books using any one of their fields (e.g. books can be searched for using id, title or author). 
The search must work using case-insensitive, partial string matching, and must return all matching items.

4.Create statistics:
    a. Most rented books. This will provide the list of books, sorted in descending order of the number of times 
    they were rented.
    b. Most active clients. This will provide the list of clients, sorted in descending order of the number of 
    book rental days they have (e.g. having 2 rented books for 3 days each counts as 2 x 3 = 6 days).
    c. Most rented author. This provides the list of book authors, sorted in descending order of the number of rentals 
    their books have.

5.Unlimited undo/redo functionality. Each step will undo/redo the previous operation performed by the user. 
Undo/redo operations must cascade and have a memory-efficient implementation (no superfluous list copying)."""

if __name__ == '__main__':
    book_validator = BookValidator()
    book_repo = BookRepository()
    book_service = BookService(book_repo, book_validator)

    client_validator = ClientValidator()
    client_repo = ClientRepository()
    client_service = ClientService(client_repo, client_validator)

    rental_validator = RentalValidator()
    rental_repo = RentalRepository()
    rental_service = RentalService(rental_repo, book_repo, client_repo, rental_validator)

    statistics_service = StatisticsService(book_repo, client_repo, rental_repo)

    undo_redo_service = UndoRedoService(book_service, client_service, rental_service)

    console = Console(book_service, client_service, rental_service, statistics_service, undo_redo_service)
    console.run_console()
