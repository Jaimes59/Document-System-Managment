from logic.classes.edoc import Edoc

class Magazine(Edoc):
    """
    A class that represents a magazine
    """
    def __init__(self, id_doc: int = 0, author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp',
                 pub_date: str = 'pub_date', size: float = 0.1, doi: str = 'doi',
                 edition: int = 1, pages: int = 1) -> object:
        """
        Constructor of the class
        :param id_doc: the id of the magazine
        :type id_doc: int
        :param author: the author of the magazine
        :type author: str
        :param title: the title of the magazine
        :type title: str
        :param price: the price of the magazine
        :type price: float
        :param topi: the topic of the magazine
        :type topi: str
        :param language: the language of the magazine
        :type language: str
        :param pub_date: the publication date of the magazine
        :type pub_date: str
        :param size: the size of the magazine
        :type size: float
        :param doi: the doi of the magazine
        :type doi: str
        :param edition: the edition of the magazine
        :type edition: int
        :param pages: the number of pages of the magazine
        :type pages: int
        """
        super().__init__(id_doc, author, title, price, topic, language, pub_date, size, doi)
        self.__edition = edition
        self.__pages = pages

    @property
    def edition(self) -> int:
        """
        Getter of the edition
        :return: the edition of the magazine
        :rtype: int
        """
        return self.__edition
    
    @edition.setter
    def edition(self, edition: int) -> None:
        """
        Setter of the edition
        :param edition: the edition of the magazine
        :type edition: int
        """
        self.__edition = edition

    @property
    def pages(self) -> int:
        """
        Getter of the pages
        :return: the number of pages of the magazine
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter of the pages
        :param pages: the number of pages of the magazine
        :type pages: int
        """
        self.__pages = pages

    def __str__(self) -> str:
        """
        Method to represent the object as a string
        :return: the string representation of the object
        :rtype: str
        """
        return {"id": self.id_doc, "Author": self.author, "Title": self.title, "Price": self.price, "Topic": self.topic,
                "Language": self.language, "Publication Date": self.pub_date, "Size": self.size, "DOI": self.doi,
                "Edition": self.edition, "Pages": self.pages}

    def __eq__(self, other: object) -> bool:
        """
        Method to compare two objects
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Magazine):
            return super().__eq__(other) and self.__edition == other.__edition and self.__pages == other.__pages
        return False