
class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name

    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, id_value):
        self.__client_id = id_value

    @property
    def client_name(self):
        return self.__client_name

    @client_name.setter
    def client_name(self, name):
        self.__client_name = name

    def __str__(self):
        return "ID:% s ,Name:% s" % (self.__client_id, self.__client_name)
