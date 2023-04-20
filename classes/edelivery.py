from classes.delivery import Delivery
from classes.person import Person

class EDelivery(Delivery):
    """
    Class that represents a delivery
    """

    def __init__(self, buyer: Person = Person(), deliver_id: int = 0,
                date: str = 'date', deliverMail: str = 'deliverMail') -> object:
        """
        Constructor of the class
        :param buyer: the buyer of the delivery
        :type buyer: Person
        :param deliver_id: the id of the delivery
        :type deliver_id: int
        :param date: the date of the delivery
        :type date: str
        :param deliverMail: the email of the delivery
        :type deliverMail: str
        """
        super().__init__(buyer, deliver_id, date)
        self.__deliverMail = deliverMail
    
    @property
    def deliverMail(self) -> str:
        """
        Getter of the email
        :return: the email of the delivery
        :rtype: str
        """
        return self.__deliverMail
    
    @deliverMail.setter
    def deliverMail(self, deliverMail: str) -> None:
        """
        Setter of the email
        :param deliverMail: the email of the delivery
        :type deliverMail: str
        """
        self.__deliverMail = deliverMail

    def sendDocument(self) -> None:
        """
        Method that sends the document
        """
        print('Sending document by email...')

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return {"ID": self.deliver_id,
                "Date": self.date,
                "Email": self.deliverMail}

    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the object to compare
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, EDelivery):
            return (super().__eq__(other) and
                    self.deliverMail == other.deliverMail)
        return False