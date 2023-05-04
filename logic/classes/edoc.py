from logic.classes.document import Document

class Edoc(Document):
    """
    A class that represents an electronic document
    """
    def __init__(self, id: int = 0, author: str = 'author',
                title: str = 'title', price: float = 0.1,
                topic: str = 'topic', language: str = 'esp',
                pub_date: str = 'pub_date', size: float = 0.1, doi: str = 'doi') -> object:
        """
        Constructor of the class
        :param id: the id of the document
        :type id: int
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
        :param pub_date: the publication date of the document
        :type pub_date: str
        :param size: the size of the document
        :type size: float
        :param doi: the doi of the document
        :type doi: str
        """
        super().__init__(id, author, title, price, topic, language)
        self.__pub_date = pub_date
        self.__size = size
        self.__doi = doi
    
    @property
    def pub_date(self) -> str:
        """
        Getter of the publication date
        :return: the publication date of the document
        :rtype: str
        """
        return self.__pub_date
    
    @pub_date.setter
    def pub_date(self, pub_date: str) -> None:
        """
        Setter of the publication date
        :param pub_date: the publication date of the document
        :type pub_date: str
        """
        self.__pub_date = pub_date

    @property
    def size(self) -> float:
        """
        Getter of the size
        :return: the size of the document
        :rtype: float
        """
        return self.__size
    
    @size.setter
    def size(self, size: float) -> None:
        """
        Setter of the size
        :param size: the size of the document
        :type size: float
        """
        self.__size = size

    @property
    def doi(self) -> str:
        """
        Getter of the doi
        :return: the doi of the document
        :rtype: str
        """
        return self.__doi
    
    @doi.setter
    def doi(self, doi: str) -> None:
        """
        Setter of the doi
        :param doi: the doi of the document
        :type doi: str
        """
        self.__doi = doi
    
    def lease(self, days: int) -> float:
        """
        Method that calculates the lease of the document
        :param days: the number of days of the lease
        :type days: int
        :return: the price of the lease
        :rtype: float
        """
        return self.price * days
    
    def __str__(self) -> str:
        """
        Method that represents the object as a string
        :return: the string representation of the object
        :rtype: str
        """
        return {"ID": self.id_doc,
                "Author": self.author,
                "Title": self.title,
                "Price": self.price,
                "Topic": self.topic,
                "Language": self.language,
                "Publication Date": self.pub_date,
                "Size": self.size,
                "DOI": self.doi}

    def __eq__(self, other: object) -> bool:
        """
        Method that returns True if the object is equal to other
        :param other: the other object
        :type other: object
        :return: True if the object is equal to other
        :rtype: bool
        """
        if isinstance(other, Edoc):
            return self.id == other.id and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language and self.pub_date == other.pub_date and self.size == other.size and self.doi == other.doi
        return False