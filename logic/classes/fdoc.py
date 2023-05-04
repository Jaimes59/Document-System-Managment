from logic.classes.document import Document

class Fdoc(Document):
    """
    A class that represents a printed document
    """
    def __init__(self, id_doc: int = '0', author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp',
                 publisher: str = 'publisher') -> object:
        """
        Constructor of the class
        :param id_doc: the id_doc of the document
        :type id_doc: int
        :param author: the author of the document
        :type author: str
        :param title: the title of the document
        :type title: str
        :param price: the price of the document
        :type price: float
        :param topi: the topic of the document
        :type topi: str
        :param language: the language of the document
        :type language: str
        :param publisher: the publisher of the document
        :type publisher: str
        """
        super().__init__(id_doc, author, title, price, topic, language)
        self.__publisher = publisher

    @property
    def publisher(self) -> str:
        """
        Getter of the publisher
        :return: the publisher of the document
        :rtype: str
        """
        return self.__publisher
    
    @publisher.setter
    def publisher(self, publisher: str) -> None:
        """
        Setter of the publisher
        :param publisher: the publisher of the document
        :type publisher: str
        """
        self.__publisher = publisher

    def __str__(self) -> str:
        """
        Method that returns the string representation of the object
        :return: the string representation of the object
        :rtype: str
        """
        return {"ID": self.id_doc,
                "Author": self.author,
                "Title": self.title,
                "Price": self.price,
                "Topic": self.topic,
                "Language": self.language,
                "Publisher": self.publisher}

    def __eq__ (self, other: object) -> bool:
        """
        Method that returns True if the object is equal to other
        :param other: the other object
        :type other: object
        :return: True if the object is equal to other
        :rtype: bool
        """
        if isinstance(other, Fdoc):
            return self.id_doc == other.id_doc and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language and self.publisher == other.publisher
        return False