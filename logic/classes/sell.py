from logic.classes.document import Document


class Sell(object):
    """
    A class that represents a sell
    """
    def __init__(self, sell_id: int = 0, date: str = 'str',
                 pay_method: str = 'pay_method', total_price: float = 0.1,
                 items: list = [Document()]) -> object:
        """
        Constructor of the class
        :param sell_id: the id of the sell
        :type sell_id: int
        :param date: the date of the sell
        :type date: str
        :param pay_method: the pay method of the sell
        :type pay_method: str
        :param total_price: the total price of the sell
        :type total_price: float
        :param items: the items of the sell
        :type items: list
        """
        self.__sell_id = sell_id
        self.__date = date
        self.__pay_method = pay_method
        self.__total_price = total_price
        self.__items = items

    @property
    def sell_id(self) -> int:
        """
        Getter of the id
        :return: the id of the sell
        :rtype: int
        """
        return self.__sell_id
    
    @sell_id.setter
    def sell_id(self, sell_id: int) -> None:
        """
        Setter of the id
        :param sell_id: the id of the sell
        :type sell_id: int
        """
        self.__sell_id = sell_id

    @property
    def date(self) -> str:
        """
        Getter of the date
        :return: the date of the sell
        :rtype: str
        """
        return self.__date
    
    @date.setter
    def date(self, date: str) -> None:
        """
        Setter of the date
        :param date: the date of the sell
        :type date: str
        """
        self.__date = date

    @property
    def pay_method(self) -> str:
        """
        Getter of the pay method
        :return: the pay method of the sell
        :rtype: str
        """
        return self.__pay_method
    
    @pay_method.setter
    def pay_method(self, pay_method: str) -> None:
        """
        Setter of the pay method
        :param pay_method: the pay method of the sell
        :type pay_method: str
        """
        self.__pay_method = pay_method

    @property
    def total_price(self) -> float:
        """
        Getter of the total price
        :return: the total price of the sell
        :rtype: float
        """
        return self.__total_price
    
    @total_price.setter
    def total_price(self, total_price: float) -> None:
        """
        Setter of the total price
        :param total_price: the total price of the sell
        :type total_price: float
        """
        self.__total_price = total_price

    @property
    def items(self) -> list:
        """
        Getter of the items
        :return: the items of the sell
        :rtype: list
        """
        return self.__items
    
    @items.setter
    def items(self, items: list) -> None:
        """
        Setter of the items
        :param items: the items of the sell
        :type items: list
        """
        self.__items = items

    def genPaycheck(self) -> None:
        """
        Generate a paycheck
        """
        print('Paycheck generated')

    def genDelivery(self) -> None:
        """
        Generate a delivery
        """
        print('Delivery generated')

    def __str__(self) -> str:
        """
        String representation of the class
        :return: the string representation of the class
        :rtype: str
        """
        return {"Sell": self.sell_id, "Date": self.date, "Payment Method": self.pay_method,
                "Total Price": self.total_price, "Items": self.items}
