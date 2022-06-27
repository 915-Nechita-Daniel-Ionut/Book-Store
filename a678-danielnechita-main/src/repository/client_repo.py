
import copy


class ClientRepository(object):
    """ This is the repository of clients. Here are the client's info stored"""
    def __init__(self):
        self.__clients = {}

    def __len__(self):
        return len(self.__clients)

    def find_by_id(self, client_id):
        """ Function for finding a client by his/hers id"""
        if client_id in self.__clients:
            return self.__clients[client_id]
        return None

    def name_getter(self, client_id):
        return self.__clients[client_id].client_name

    def save_client(self, client):
        """ Function for saving a client in the repository"""
        self.__clients[client.client_id] = client

    def update(self, client_id_to_update, client_update):
        """ Function for updating the information about a client"""
        for client_id in self.__clients:
            if client_id_to_update == client_id:
                self.__clients[client_id] = client_update

    def delete_client_by_id(self, id_to_delete):
        """ Function for deleting a client"""
        client_list_copy = copy.deepcopy(self.__clients)
        for client_id in client_list_copy:
            if id_to_delete == client_id:
                del self.__clients[client_id]

    def get_all_clients(self):
        """ Function for getting the list of clients"""
        return self.__clients
