from typing import Dict

from logic.classes.delivery import Delivery
from logic.classes.person import Person


class EDelivery(Delivery):
    """
    Class that represents a delivery
    """

    def __init__(self, buyer: Person = Person(), deliver_id: int = 0,
                 date: str = 'date', deliver_mail: str = 'deliverMail') -> object:
        """
        Constructor of the class
        :param buyer: the buyer of the delivery
        :type buyer: Person
        :param deliver_id: the id of the delivery
        :type deliver_id: int
        :param date: the date of the delivery
        :type date: str
        :param deliver_mail: the email of the delivery
        :type deliver_mail: str
        """
        super().__init__(buyer, deliver_id, date)
        self.__deliver_mail = deliver_mail
    
    @property
    def deliver_mail(self) -> str:
        """
        Getter of the email
        :return: the email of the delivery
        :rtype: str
        """
        return self.__deliver_mail
    
    @deliver_mail.setter
    def deliver_mail(self, deliver_mail: str) -> None:
        """
        Setter of the email
        :param deliver_mail: the email of the delivery
        :type deliver_mail: str
        """
        self.__deliver_mail = deliver_mail

    def sendDocument(self) -> None:
        """
        Method that sends the document
        """
        print('Sending document by email...')

    def __str__(self) -> dict[str, str | int]:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return {"ID": self.deliver_id,
                "Date": self.date,
                "Email": self.deliver_mail}

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