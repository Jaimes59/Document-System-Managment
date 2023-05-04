from logic.classes.person import Person

class Delivery (object):
    """
    Class that represents a delivery
    """

    def __init__ (self, buyer: Person = Person(), deliver_id: int = 0, date: str = 'date') -> object:
        """
        Constructor of the class
        :param buyer: the buyer of the delivery
        :type buyer: Person
        :param deliver_id: the id of the delivery
        :type deliver_id: int
        :param date: the date of the delivery
        :type date: str
        """
        self.__buyer = buyer
        self.__deliver_id = deliver_id
        self.__date = date
    
    @property
    def buyer(self) -> Person:
        """
        Getter of the buyer
        :return: the buyer of the delivery
        :rtype: Person
        """
        return self.__buyer
    
    @buyer.setter
    def buyer(self, buyer: Person) -> None:
        """
        Setter of the buyer
        :param buyer: the buyer of the delivery
        :type buyer: Person
        """
        self.__buyer = buyer

    @property
    def deliver_id(self) -> int:
        """
        Getter of the id
        :return: the id of the delivery
        :rtype: int
        """
        return self.__deliver_id
    
    @deliver_id.setter
    def deliver_id(self, deliver_id: int) -> None:
        """
        Setter of the id
        :param deliver_id: the id of the delivery
        :type deliver_id: int
        """
        self.__deliver_id = deliver_id

    @property
    def date(self) -> str:
        """
        Getter of the date
        :return: the date of the delivery
        :rtype: str
        """
        return self.__date
    
    @date.setter
    def date(self, date: str) -> None:
        """
        Setter of the date
        :param date: the date of the delivery
        :type date: str
        """
        self.__date = date

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return {"ID": self.deliver_id,
                "Date": self.date,
                "Buyer": self.buyer}

    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Delivery):
            return (self.deliver_id == other.deliver_id and 
                    self.date == other.date and self.buyer == other.buyer)
        return False