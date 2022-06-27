from src.domain.rental_entity import Rental
from src.validators.validator_exception import ValidatorException


class RentalValidator:
    @staticmethod
    def validate(rental):
        errors = ""
        if isinstance(rental, Rental) is False:
            errors += "It is not a rental! \n"
        if int(rental.rental_id) < 1:
            errors += "Id must be a positive integer \n"
        if rental.rented_date == "":
            errors += "Rented date can't be empty! \n"
        if rental.returned_date == "":
            errors += "Returned date can't be empty! \n"
        if errors != "":
            raise ValidatorException(errors)