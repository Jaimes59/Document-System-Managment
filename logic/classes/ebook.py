from logic.classes.edoc import Edoc

class Ebook(Edoc):
    """
    A class that represents an electronic book
    """
    def __init__(self, id_doc: int = 0, author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp',
                 pub_date: str = 'pub_date', size: float = 0.1, doi: str = 'doi',
                 editor: str = 'editor', pages: int = 1, synopsis: str = 'synopsis') -> object:
        """
        Constructor of the class
        :param id_doc: the id of the electronic book
        :type id_doc: int
        :param author: the author of the electronic book
        :type author: str
        :param title: the title of the electronic book
        :type title: str
        :param price: the price of the electronic book
        :type price: float
        :param topi: the topic of the electronic book
        :type topi: str
        :param language: the language of the electronic book
        :type language: str
        :param pub_date: the publication date of the electronic book
        :type pub_date: str
        :param size: the size of the electronic book
        :type size: float
        :param doi: the doi of the electronic book
        :type doi: str
        :param editor: the editor of the electronic book
        :type editor: str
        :param pages: the number of pages of the electronic book
        :type pages: int
        :param synopsis: the synopsis of the electronic book
        :type synopsis: str
        """
        super().__init__(id_doc, author, title, price, topic, language, pub_date, size, doi)
        self.__editor = editor
        self.__pages = pages
        self.__synopsis = synopsis
    
    @property
    def editor(self) -> str:
        """
        Getter of the editor
        :return: the editor of the book
        :rtype: str
        """
        return self.__editor
    
    @editor.setter
    def editor(self, editor: str) -> None:
        """
        Setter of the editor
        :param editor: the editor of the book
        :type editor: str
        """
        self.__editor = editor
    
    @property
    def pages(self) -> int:
        """
        Getter of the number of pages
        :return: the number of pages of the book
        :rtype: int
        """
        return self.__pages
    
    @pages.setter
    def pages(self, pages: int) -> None:
        """
        Setter of the number of pages
        :param pages: the number of pages of the book
        :type pages: int
        """
        self.__pages = pages

    @property
    def synopsis(self) -> str:
        """
        Getter of the synopsis
        :return: the synopsis of the book
        :rtype: str
        """
        return self.__synopsis
    
    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter of the synopsis
        :param synopsis: the synopsis of the book
        :type synopsis: str
        """
        self.__synopsis = synopsis

    def __str__(self) -> str:
        """
        Method to print the object
        :return: the string to print
        :rtype: str
        """
        return {"ID": self.id_doc,
                "Author": self.author,
                "Title": self.title,
                "Price": self.price,
                "Topic": self.topic,
                "Language": self.language,
                "Editor": self.editor,
                "Pages": self.pages,
                "Synopsis": self.synopsis}

    def __eq__(self, other: object) -> bool:
        """
        Method to compare two objects
        :param other: the other object to compare
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, Ebook):
            return super().__eq__(other) and self.__editor == other.editor and self.__pages == other.pages and self.__synopsis == other.synopsis
        return False