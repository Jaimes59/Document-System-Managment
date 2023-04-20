class Document(object):
    """
    A class that represents a document
    """

    def __init__(self, id_doc: int = 0, author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp') -> object:
        """
        Constructor of the class
        :param id_doc: the id of the document
        :type id_doc: int
        :param author: the author of the document
        :type author: str
        :param title: the title of the document
        :type title: str
        :param price: the price of the document
        :type price: float
        :param topic: the topic of the document
        :type topic: str
        :param language: the language of the document
        :type language: str
        """
        self.__id_doc = id_doc
        self.__author = author
        self.__title = title
        self.__price = price
        self.__topic = topic
        self.__language = language

    @property
    def id_doc(self) -> int:
        """
        Getter of the id_doc
        :return: the id_doc of the document
        :rtype: int
        """
        return self.__id_doc

    @id_doc.setter
    def id_doc(self, id_doc: int) -> None:
        """
        Setter of the id_doc
        :param id_doc: the id_doc of the document
        :type id_doc: int
        """
        self.__id_doc = id_doc

    @property
    def author(self) -> str:
        """
        Getter of the author
        :return: the author of the document
        :rtype: str
        """
        return self.__author

    @author.setter
    def author(self, author: str) -> None:
        """
        Setter of the author
        :param author: the author of the document
        :type author: str
        """
        self.__author = author

    @property
    def title(self) -> str:
        """
        Getter of the title
        :return: the title of the document
        :rtype: str
        """
        return self.__title

    @title.setter
    def title(self, title: str) -> None:
        """
        Setter of the title
        :param title: the title of the document
        :type title: str
        """
        self.__title = title

    @property
    def price(self) -> float:
        """
        Getter of the price
        :return: the price of the document
        :rtype: float
        """
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        """
        Setter of the price
        :param price: the price of the document
        :type price: float
        """
        self.__price = price

    @property
    def topic(self) -> str:
        """
        Getter of the topic
        :return: the topic of the document
        :rtype: str
        """
        return self.__topic

    @topic.setter
    def topic(self, topic: str) -> None:
        """
        Setter of the topic
        :param topic: the topic of the document
        :type topic: str
        """
        self.__topic = topic

    @property
    def language(self) -> str:
        """
        Getter of the language
        :return: the language of the document
        :rtype: str
        """
        return self.__language

    @language.setter
    def language(self, language: str) -> None:
        """
        Setter of the language
        :param language: the language of the document
        :type language: str
        """
        self.__language = language

    def buy(self, quantity: int) -> float:
        """
        Method that calculates the total price of a document
        :param quantity: the quantity of documents
        :type quantity: int
        :return: the total price of the documents
        :rtype: float
        """
        return self.price * quantity

    def __str__(self) -> str:
        """
        Method that returns a string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return{"id": self.id_doc, "Author": self.author, "Title": self.title, "Price": self.price, "Topic": self.topic,
               "Language": self.language}


    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Document):
            return self.id_doc == other.id_doc and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language
        return False
