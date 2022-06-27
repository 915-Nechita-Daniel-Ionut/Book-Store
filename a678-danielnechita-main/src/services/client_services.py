from src.domain.client_entity import Client
from src.domain.exception_classes import *


class ClientService:
    """This is a service class for clients, storing them in a repository and adding/removing,
    updating and listing the clients"""
    def __init__(self, client_repo, client_validator):
        self.__client_repo = client_repo
        self.__client_validator = client_validator

    def add_client(self, client_id, client_name):
        """ Function for adding a client to the list"""
        client = Client(client_id, client_name)
        self.__client_validator.validate(client)
        if self.__client_repo.find_by_id(client_id) is None:
            self.__client_repo.save_client(client)
        else:
            raise IdAlreadyExistsException

    def client_name_getter(self, client_id):
        try:
            client_name = self.__client_repo.name_getter(client_id)
            return client_name
        except KeyError:
            raise IdNotFoundException

    def client_list_getter(self):
        """ Function for getting the list of clients"""
        client_list = self.__client_repo.get_all_clients()
        return client_list

    def remove_client(self, client_id_to_delete):
        """ Function for removing a clients from the list"""
        if self.__client_repo.find_by_id(client_id_to_delete) is not None:
            self.__client_repo.delete_client_by_id(client_id_to_delete)
        else:
            raise IdNotFoundException

    def client_update(self, client_id_to_update, name_update):
        """ Function for updating a client's name"""
        client = Client(client_id_to_update, name_update)
        self.__client_validator.validate(client)
        if self.__client_repo.find_by_id(client_id_to_update) is not None:
            self.__client_repo.update(client_id_to_update, client)
        else:
            raise IdNotFoundException

    def search_client_by_id(self, searched_id):
        if not searched_id.isnumeric():
            raise IdIsNotNumericException
        client_list = self.client_list_getter()
        search_client_list = []
        for client_id in client_list:
            client = client_list[client_id]
            if searched_id in str(client.client_id):
                search_client_list.append(client)
        return search_client_list

    def search_client_by_name(self, searched_name):
        client_list = self.client_list_getter()
        search_client_list = []
        for client_name in client_list:
            client = client_list[client_name]
            if searched_name.lower() in client.client_name.lower():
                search_client_list.append(client)
        return search_client_list
