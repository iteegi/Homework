# Task 6.7

from math import ceil


def type_prop(name, expected_type):
    """Argument type validator

    Args:
        name (str): argument name
        expected_type (class): expected type

    Raises:
        TypeError: when expected type and actual type do not match

    Returns:
        property: property
    """
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop


class lazyproperty:
    """Lazily evaluated property.

    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Pagination:
    """Stores page pagination."""

    amount = type_prop('amount', int)
    text = type_prop('text', str)

    def __init__(self, text, amount) -> None:
        """Initializer for class Pagination.

        Args:
            text (str): text that is paginated.
            amount (int): how many symbols will be allowed per each page.
        """
        self.text = text
        self.amount = amount

    @lazyproperty
    def page_count(self):
        """Get number of pages.

        Returns:
            int: number of pages.
        """
        return ceil(len(self.text)/self.amount)

    @lazyproperty
    def item_count(self):
        """Get number of characters in the text.

        Returns:
            int: number of characters in the text.
        """
        return len(self.text)

    def count_items_on_page(self, page):
        """Get number of items per page.

        Args:
            page (int): page number.

        Raises:
            Exception: when the wrong page is given.

        Returns:
            int: number of characters on a particular page.
        """
        a = self.page_count - 1
        if 0 <= page <= a:
            if a == page:
                return len(self.text) % self.amount
            return self.amount
        raise Exception(f'Invalid index. Page is missing.')

    def find_page(self, word: str):
        """Finds the page numbers on which the given word is mentioned.

        Args:
            word (str): search word

        Raises:
            Exception: when a word is missing from the text

        Returns:
            List[int]: numbers of pages on which the word is mentioned.
        """

        len_word = len(word)
        pages = []
        start = 0

        while True:
            stop = self.text.find(word, start)
            if stop == -1:
                break
            else:
                min_page = stop // self.amount
                max_page = (stop + len_word - 1) // self.amount
                if stop == max_page:
                    pages.append(min_page)
                else:
                    while min_page <= max_page:
                        pages.append(min_page)
                        min_page += 1

                start = stop + len_word
        if pages:
            return pages
        raise Exception(f"'{word}' is missing on the pages")

    def display_page(self, page):
        """Displays text on a given page.

        Args:
            page (int): desired page.

        Raises:
            Exception: when there is no information.

        Returns:
            str: page text.
        """
        s = self.text[self.amount*page:self.amount*page+self.amount]
        if s:
            return s
        raise Exception('No data')
