"""
Specials pages
"""

from book_core import Special


class SpecialPages(Special):
    """
    Special pages class
    """

    _title = "The book title"
    _final = "The book final"
    _cover = "The book cover"
    _resume = "The book resume"

    def title(self) -> str:
        """
        :return: the book title
        """

        return self._title

    def final(self) -> str:
        """
        :return: the book final page
        """

        return self._final

    def cover(self) -> str:
        """
        :return: the book cover
        """

        return self._cover

    def resume(self) -> str:
        """
        :return: the book resume
        """

        return self._resume
