from logic.classes.document import Document


class Lease(object):
    """
    A class that represents a lease
    """

    def __init__(self, lease_id: int = 0, start_date: str = 'start_date',
                 finish_date: str = 'finish_date', pay_method: str = 'pay_method',
                 total_price: float = 0.1, items: list = [Document()]) -> object:
        """
        Constructor of the class
        :param lease_id: the id of the lease
        :type lease_id: int
        :param start_date: the start date of the lease
        :type start_date: str
        :param finish_date: the finish date of the lease
        :type finish_date: str
        :param pay_method: the pay method of the lease
        :type pay_method: str
        :param total_price: the total price of the lease
        :type total_price: float
        :param items: the items of the lease
        :type items: list
        """
        self.__lease_id = lease_id
        self.__start_date = start_date
        self.__finish_date = finish_date
        self.__pay_method = pay_method
        self.__total_price = total_price
        self.__items = items

    @property
    def lease_id(self) -> int:
        """
        Getter of the id
        :return: the id of the lease
        :rtype: int
        """
        return self.__lease_id

    @lease_id.setter
    def lease_id(self, lease_id: int) -> None:
        """
        Setter of the id
        :param lease_id: the id of the lease
        :type lease_id: int
        """
        self.__lease_id = lease_id

    @property
    def start_date(self) -> str:
        """
        Getter of the start date
        :return: the start date of the lease
        :rtype: str
        """
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date: str) -> None:
        """
        Setter of the start date
        :param start_date: the start date of the lease
        :type start_date: str
        """
        self.__start_date = start_date

    @property
    def finish_date(self) -> str:
        """
        Getter of the finish date
        :return: the finish date of the lease
        :rtype: str
        """
        return self.__finish_date

    @finish_date.setter
    def finish_date(self, finish_date: str) -> None:
        """
        Setter of the finish date
        :param finish_date: the finish date of the lease
        :type finish_date: str
        """
        self.__finish_date = finish_date

    @property
    def pay_method(self) -> str:
        """
        Getter of the pay method
        :return: the pay method of the lease
        :rtype: str
        """
        return self.__pay_method

    @pay_method.setter
    def pay_method(self, pay_method: str) -> None:
        """
        Setter of the pay method
        :param pay_method: the pay method of the lease
        :type pay_method: str
        """
        self.__pay_method = pay_method

    @property
    def total_price(self) -> float:
        """
        Getter of the total price
        :return: the total price of the lease
        :rtype: float
        """
        return self.__total_price

    @total_price.setter
    def total_price(self, total_price: float) -> None:
        """
        Setter of the total price
        :param total_price: the total price of the lease
        :type total_price: float
        """
        self.__total_price = total_price

    @property
    def items(self) -> list:
        """
        Getter of the items
        :return: the items of the lease
        :rtype: list
        """
        return self.__items

    @items.setter
    def items(self, items: list) -> None:
        """
        Setter of the items
        :param items: the items of the lease
        :type items: list
        """
        self.__items = items

    def genPaycheck(self) -> None:
        """
        Generates a paycheck
        """
        print('Generating paycheck')

    def genDelivery(self) -> None:
        """
        Generates a delivery
        """
        print('Generating delivery')

    def __str__(self) -> str:
        """
        Converts the object to string
        :return: the string
        :rtype: str
        """
        return {
            "Lease ID": self.lease_id,
            "Start Date": self.start_date,
            "Finish Date": self.finish_date,
            "Payment Method": self.pay_method,
            "Total Price": self.total_price,
            "Items": self.items
        }

    def __eq__(self, other: object) -> bool:
        """
        Checks if two objects are equal
        :param other: the other object
        :type other: object
        :return: True if they are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Lease):
            return (self.__lease_id == other.lease_id and
                    self.__start_date == other.start_date and
                    self.__finish_date == other.finish_date and
                    self.__pay_method == other.pay_method and
                    self.__total_price == other.total_price and
                    self.__items == other.items)
        return False
