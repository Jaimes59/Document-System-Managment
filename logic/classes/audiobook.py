from logic.classes.edoc import Edoc


class AudioBook(Edoc):
    """
    A class that represents an audio book
    """

    def __init__(self, id_doc: int = 0, author: str = 'author',
                 title: str = 'title', price: float = 0.1,
                 topic: str = 'topic', language: str = 'esp',
                 pub_date: str = 'pub_date', size: float = 0.1, doi: str = 'doi',
                 hours: int = 1, minutes: int = 1, seconds: int = 1,
                 synopsis: str = 'synopsis') -> object:
        """
        Constructor of the class
        :param id_doc: the id of the audio book
        :type id_doc: int
        :param author: the author of the audio book
        :type author: str
        :param title: the title of the audio book
        :type title: str
        :param price: the price of the audio book
        :type price: float
        :param topi: the topic of the audio book
        :type topi: str
        :param language: the language of the audio book
        :type language: str
        :param pub_date: the publication date of the audio book
        :type pub_date: str
        :param size: the size of the audio book
        :type size: float
        :param doi: the doi of the audio book
        :type doi: str
        :param hours: the hours of the audio book
        :type hours: int
        :param minutes: the minutes of the audio book
        :type minutes: int
        :param seconds: the seconds of the audio book
        :type seconds: int
        :param synopsis: the synopsis of the audio book
        :type synopsis: str
        """
        super().__init__(id_doc, author, title, price, topic, language, pub_date, size, doi)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__synopsis = synopsis

    @property
    def hours(self) -> int:
        """
        Getter of the hours
        :return: the hours of the audio book
        :rtype: int
        """
        return self.__hours

    @hours.setter
    def hours(self, hours: int) -> None:
        """
        Setter of the hours
        :param hours: the hours of the audio book
        :type hours: int
        """
        self.__hours = hours

    @property
    def minutes(self) -> int:
        """
        Getter of the minutes
        :return: the minutes of the audio book
        :rtype: int
        """
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int) -> None:
        """
        Setter of the minutes
        :param minutes: the minutes of the audio book
        :type minutes: int
        """
        self.__minutes = minutes

    @property
    def seconds(self) -> int:
        """
        Getter of the seconds
        :return: the seconds of the audio book
        :rtype: int
        """
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int) -> None:
        """
        Setter of the seconds
        :param seconds: the seconds of the audio book
        :type seconds: int
        """
        self.__seconds = seconds

    @property
    def synopsis(self) -> str:
        """
        Getter of the synopsis
        :return: the synopsis of the audio book
        :rtype: str
        """
        return self.__synopsis

    @synopsis.setter
    def synopsis(self, synopsis: str) -> None:
        """
        Setter of the synopsis
        :param synopsis: the synopsis of the audio book
        :type synopsis: str
        """
        self.__synopsis = synopsis

    def __str__(self) -> str:
        """
        String representation of the class
        :return: the string representation of the class
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
                "DOI": self.doi,
                "Duration": f"{self.hours}h {self.minutes}m {self.seconds}s",
                "Synopsis": self.synopsis}


    def __eq__(self, other: object) -> bool:
        """
        Equality operator
        :param other: the other object
        :type other: object
        :return: True if the objects are equal, False otherwise
        :rtype: bool
        """
        if isinstance(other, AudioBook):
            return self.id == other.id and self.author == other.author and self.title == other.title and self.price == other.price and self.topic == other.topic and self.language == other.language and self.pub_date == other.pub_date and self.size == other.size and self.doi == other.doi and self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds and self.synopsis == other.synopsis
        return False
