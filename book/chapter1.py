
"""
Chapter 1
"""

from book_core import Chapter


class Chapter1(Chapter):
    """
    Chapter 2 definition class
    """

    _title = "Chapter 1 title"
    _content = "This is the first chapter content.\nIt is multiline.\nBecause it is a chapter, not a title"

    def title(self) -> str:
        """
        :return: the chapter title
        """

        return self._title

    def content(self) -> str:
        """
        :return: the chapter content
        """

        return self._content
