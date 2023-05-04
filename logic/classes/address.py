class Address(object):
    """
    A class that represents an address
    """

    def __init__(self, country: str = 'country', department: str = 'department',
                 city: str = 'city', post_code: str = 'post_code', neighborhood: str = 'neighborhood',
                 street: str = 'str', complement: str = 'str') -> object:
        """
        Constructor of the class
        :param country: the country of the address
        :type country: str
        :param department: the department of the address
        :type department: str
        :param city: the city of the address
        :type city: str
        :param post_code: the post code of the address
        :type post_code: str
        :param neighborhood: the neighborhood of the address
        :type neighborhood: str
        :param street: the street of the address
        :type street: str
        :param complement: the complement of the address
        :type complement: str
        """
        self.__country = country
        self.__department = department
        self.__city = city
        self.__post_code = post_code
        self.__neighborhood = neighborhood
        self.__street = street
        self.__complement = complement

    @property
    def country(self) -> str:
        """
        Getter of the country
        :return: the country of the address
        :rtype: str
        """
        return self.__country

    @country.setter
    def country(self, country: str) -> None:
        """
        Setter of the country
        :param country: the country of the address
        :type country: str
        """
        self.__country = country

    @property
    def department(self) -> str:
        """
        Getter of the department
        :return: the department of the address
        :rtype: str
        """
        return self.__department

    @department.setter
    def department(self, department: str) -> None:
        """
        Setter of the department
        :param department: the department of the address
        :type department: str
        """
        self.__department = department

    @property
    def city(self) -> str:
        """
        Getter of the city
        :return: the city of the address
        :rtype: str
        """
        return self.__city

    @city.setter
    def city(self, city: str) -> None:
        """
        Setter of the city
        :param city: the city of the address
        :type city: str
        """
        self.__city = city

    @property
    def post_code(self) -> str:
        """
        Getter of the post code
        :return: the post code of the address
        :rtype: str
        """
        return self.__post_code

    @post_code.setter
    def post_code(self, post_code: str) -> None:
        """
        Setter of the post code
        :param post_code: the post code of the address
        :type post_code: str
        """
        self.__post_code = post_code

    @property
    def neighborhood(self) -> str:
        """
        Getter of the neighborhood
        :return: the neighborhood of the address
        :rtype: str
        """
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood: str) -> None:
        """
        Setter of the neighborhood
        :param neighborhood: the neighborhood of the address
        :type neighborhood: str
        """
        self.__neighborhood = neighborhood

    @property
    def street(self) -> str:
        """
        Getter of the street
        :return: the street of the address
        :rtype: str
        """
        return self.__street

    @street.setter
    def street(self, street: str) -> None:
        """
        Setter of the street
        :param street: the street of the address
        :type street: str
        """
        self.__street = street

    @property
    def complement(self) -> str:
        """
        Getter of the complement
        :return: the complement of the address
        :rtype: str
        """
        return self.__complement

    @complement.setter
    def complement(self, complement: str) -> None:
        """
        Setter of the complement
        :param complement: the complement of the address
        :type complement: str
        """
        self.__complement = complement

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return {"country": self.country,
                "department": self.department,
                "city": self.city,
                "post_code": self.post_code,
                "neighborhood": self.neighborhood,
                "street": self.street,
                "complement": self.complement}

    def __eq__(self, other: object) -> bool:
        """
        Method that returns if the object is equal to another object
        :param other: the other object
        :type other: object
        :return: if the object is equal to another object
        :rtype: bool
        """
        if isinstance(other, Address):
            return self.country == other.country and self.department == other.department and self.city == other.city and self.post_code == other.post_code and self.neighborhood == other.neighborhood and self.street == other.street and self.complement == other.complement
        return False
