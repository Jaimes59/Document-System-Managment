from typing import Dict, Any

from logic.classes.edoc import Edoc


class InvBook(Edoc):
    """
    A class that represents an inventory book
    """

    def __init__(self, id_doc: int = 0, author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp',
                 pub_date: str = 'pub_date', size: float = 0.1, doi: str = 'doi',
                 pages: int = 1, abstract: str = 'abstract') -> object:
        """
        Constructor of the class
        :param id_doc: the id of the InvBook
        :type id_doc: int
        :param author: the author of the InvBook
        :type author: str
        :param title: the title of the InvBook
        :type title: str
        :param price: the price of the InvBook
        :type price: float
        :param topi: the topic of the InvBook
        :type topi: str
        :param language: the language of the InvBook
        :type language: str
        :param pub_date: the publication date of the InvBook
        :type pub_date: str
        :param size: the size of the InvBook
        :type size: float
        :param doi: the doi of the InvBook
        :type doi: str
        :param pages: the number of pages of the InvBook
        :type pages: int
        :param abstract: the abstract of the InvBook
        :type abstract: str
        """
        super().__init__(id_doc, author, title, price, topic, language, pub_date, size, doi)
        self.__pages = pages
        self.__abstract = abstract

    @property
    def pages(self) -> int:
        """
        Getter of the pages
        :return: the pages of the book
        :rtype: int
        """
        return self.__pages

    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter of the pages
        :param pages: the pages of the book
        :type pages: int
        """
        self.__pages = pages

    @property
    def abstract(self) -> str:
        """
        Getter of the abstract
        :return: the abstract of the book
        :rtype: str
        """
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str) -> None:
        """
        Setter of the abstract
        :param abstract: the abstract of the book
        :type abstract: str
        """
        self.__abstract = abstract

    def __str__(self) -> dict[str | Any, int | str | float | Any]:
        """
        Method that represents the object as a string
        :return: the string representation of the object
        :rtype: str
        """
        return {"id": self.id_doc,
                "Author": self.author,
                "Title": self.title,
                "Price": self.price,
                "Topic": self.topic,
                "Language": self.language,
                "Publication Date": self.pub_date,
                "Size": self.size,
                "DOI": self.doi,
                "Pages": self.pages,
                "Abstract": self.abstract
                }

    def __eq__(self, other: object) -> bool:
        """
        Method that compares two objects
        :param other: the object to compare
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, InvBook):
            return self.id == other.id and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language and self.pub_date == other.pub_date and self.size == other.size and self.doi == other.doi and self.pages == other.pages and self.abstract == other.abstract
        else:
            return False
