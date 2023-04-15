class Person (object):
    """
    A class that represents a person
    """

    def __init__(self, id: int = 0, name: str = 'name', 
                last_name: str = 'last_name', phone: str = 'phone',
                mail: str = 'mail') -> object:
        """
        Constructor of the class
        :param id: the id of the person
        :type id: int
        :param name: the name of the person
        :type name: str
        :param last_name: the last name of the person
        :type last_name: str
        :param phone: the phone of the person
        :type phone: str
        :param mail: the mail of the person
        :type mail: str
        """
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__phone = phone
        self.__mail = mail
    
    @property
    def id(self) -> int:
        """
        Getter of the id
        :return: the id of the person
        :rtype: int
        """
        return self.__id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Setter of the id
        :param id: the id of the person
        :type id: int
        """
        self.__id = id
    
    @property
    def name(self) -> str:
        """
        Getter of the name
        :return: the name of the person
        :rtype: str
        """
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        """
        Setter of the name
        :param name: the name of the person
        :type name: str
        """
        self.__name = name
    
    @property
    def last_name(self) -> str:
        """
        Getter of the last name
        :return: the last name of the person
        :rtype: str
        """
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """
        Setter of the last name
        :param last_name: the last name of the person
        :type last_name: str
        """
        self.__last_name = last_name

    @property
    def phone(self) -> str:
        """
        Getter of the phone
        :return: the phone of the person
        :rtype: str
        """
        return self.__phone
    
    @phone.setter
    def phone(self, phone: str) -> None:
        """
        Setter of the phone
        :param phone: the phone of the person
        :type phone: str
        """
        self.__phone = phone

    @property
    def mail(self) -> str:
        """
        Getter of the mail
        :return: the mail of the person
        :rtype: str
        """
        return self.__mail
    
    @mail.setter
    def mail(self, mail: str) -> None:
        """
        Setter of the mail
        :param mail: the mail of the person
        :type mail: str
        """
        self.__mail = mail

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return f'Person: {self.id}, {self.name}, {self.last_name}, {self.phone}, {self.mail}'
    
    def __eq__(self, other: object) -> bool:
        """
        Method that returns if two objects are equal
        :param other: the other object
        :type other: object
        :return: if the objects are equal
        :rtype: bool
        """
        if isinstance(other, Person):
            return (self.id == other.id and self.name == other.name and
                    self.last_name == other.last_name and 
                    self.phone == other.phone and self.mail == other.mail)
        return False