from logic.classes.document import Document
from logic.classes.administrator import Administrator
from logic.classes.client import Client

class DMS(object):
    """
    Class that represents a document management system
    """

    def __init__(self, catalog: list = [Document()], users: list = [Client()],
                 administrators: list = [Administrator()]) -> object:
        """
        Constructor of the class
        :param catalog: the catalog of the system
        :type catalog: list
        :param users: the users of the system
        :type users: list
        :param administrators: the administrators of the system
        :type administrators: list
        """
        self.__catalog = catalog
        self.__users = users
        self.__administrators = administrators

    @property
    def catalog(self) -> list:
        """
        Getter of the catalog
        :return: the catalog of the system
        :rtype: list
        """
        return self.__catalog
    
    @catalog.setter
    def catalog(self, catalog: list) -> None:
        """
        Setter of the catalog
        :param catalog: the catalog of the system
        :type catalog: list
        """
        self.__catalog = catalog
    
    @property
    def users(self) -> list:
        """
        Getter of the users
        :return: the users of the system
        :rtype: list
        """
        return self.__users
    
    @users.setter
    def users(self, users: list) -> None:
        """
        Setter of the users
        :param users: the users of the system
        :type users: list
        """
        self.__users = users

    @property
    def administrators(self) -> list:
        """
        Getter of the administrators
        :return: the administrators of the system
        :rtype: list
        """
        return self.__administrators
    
    @administrators.setter
    def administrators(self, administrators: list) -> None:
        """
        Setter of the administrators
        :param administrators: the administrators of the system
        :type administrators: list
        """
        self.__administrators = administrators

    def createUser(self, user: Client) -> None:
        """
        Method that creates a user
        :param user: the user to be created
        :type user: Client
        """
        self.__users.append(user)

    def createAdministrator(self, administrator: Administrator) -> None:
        """
        Method that creates an administrator
        :param administrator: the administrator to be created
        :type administrator: Administrator
        """
        self.__administrators.append(administrator)

    def __str__(self) -> str:
        """
        Method that returns a string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        #Printing the list of catalog
        catalog = ''
        for document in self.catalog:
            catalog += f'{document}'
        #Printing the list of users
        users = ''
        for user in self.users:
            users += f'{user}'
        #Printing the list of administrators
        administrators = ''
        for administrator in self.administrators:
            administrators += f'{administrator}'
        return (f'***Printing DMS***'
                f'\nCatalog: \n{catalog}'
                f'\nUsers: \n{users}'
                f'\nAdministrators: \n{administrators}')
    
    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the other object
        :type other: object
        :return: True if they are equal, False otherwise
        :rtype: bool
        """
        return (self.catalog == other.catalog and self.users == other.users and
                self.administrators == other.administrators)