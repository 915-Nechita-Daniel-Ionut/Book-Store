
from src.domain.client_entity import Client
from src.validators.validator_exception import ValidatorException


class ClientValidator:
    @staticmethod
    def validate(client):
        errors = ""
        if isinstance(client, Client) is False:
            errors += "It is not a client!"
        elif int(client.client_id) < 1:
            errors += "Id must be a positive integer"
        if client.client_name == "":
            errors += "Name can't be empty!"
        if errors != "":
            raise ValidatorException(errors)
