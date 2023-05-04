from logic.classes.delivery import Delivery
from logic.classes.person import Person
from logic.classes.address import Address


class FDelivery(Delivery):
    """
    Class that represents a delivery
    """

    def __init__(self, buyer: Person = Person(), deliver_id: int = 0,
                 date: str = 'date', address: Address = Address(),
                 contact: Person = Person(), company: str = 'company') -> object:
        """
        Constructor of the class
        :param buyer: the buyer of the delivery
        :type buyer: Person
        :param deliver_id: the id of the delivery
        :type deliver_id: int
        :param date: the date of the delivery
        :type date: str
        :param address: the address of the delivery
        :type address: Address
        :param contact: the contact of the delivery
        :type contact: Person
        :param company: the company of the delivery
        :type company: str
        """
        super().__init__(buyer, deliver_id, date)
        self.__address = address
        self.__contact = contact
        self.__company = company

    @property
    def address(self) -> Address:
        """
        Getter of the address
        :return: the address of the delivery
        :rtype: Address
        """
        return self.__address
    
    @address.setter
    def address(self, address: Address) -> None:
        """
        Setter of the address
        :param address: the address of the delivery
        :type address: Address
        """
        self.__address = address
    
    @property
    def contact(self) -> Person:
        """
        Getter of the contact
        :return: the contact of the delivery
        :rtype: Person
        """
        return self.__contact
    
    @contact.setter
    def contact(self, contact: Person) -> None:
        """
        Setter of the contact
        :param contact: the contact of the delivery
        :type contact: Person
        """
        self.__contact = contact

    @property
    def company(self) -> str:
        """
        Getter of the company
        :return: the company of the delivery
        :rtype: str
        """
        return self.__company
    
    @company.setter
    def company(self, company: str) -> None:
        """
        Setter of the company
        :param company: the company of the delivery
        :type company: str
        """
        self.__company = company

    def createDelivery(self) -> None:
        """
        Method that creates a delivery
        """
        print('Delivery created')
        pass

    def __str__(self) -> str:
        """
        Method that returns the string representation of a delivery
        :return: the string representation of a delivery
        :rtype: str
        """
        return {"ID": self.deliver_id,
                "Date": self.date,
                "Buyer": self.buyer,
                "Address": self.address,
                "Contact": self.contact,
                "Company": self.company}

    def __eq__(self, other: object) -> bool:
        """
        Method that compares two deliveries
        :param other: the other delivery
        :type other: object
        :return: True if the two deliveries are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, FDelivery):
            return (self.deliver_id == other.deliver_id and
                    self.date == other.date and
                    self.buyer == other.buyer and
                    self.address == other.address and
                    self.contact == other.contact and
                    self.company == other.company)
        return False