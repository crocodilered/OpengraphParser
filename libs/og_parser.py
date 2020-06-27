"""
OpenGraph tags workout.
"""

import re


class OgParser:
    """
    Class to extract OpenGraph tags.
    """
    def __init__(self):
        self.__tag_pattern = re.compile('<meta( .+?)>', re.I)
        self.__key_pattern = re.compile(' property="og:(.+?)"', re.I)
        self.__val_pattern = re.compile(' content="(.+?)"', re.I)

    def x_tags(self, text: str) -> list:
        """
        Extract META tags from text.
        :param text: Input text to extract tags.
        :return: List with tags found.
        """
        return self.__tag_pattern.findall(text)

    def x_data(self, tag: str) -> tuple:
        """
        Extract OpenGraph @property and @content from tag.
        :param tag:
        :return: Tuple with @property and @content values.
        """
        key, val = None, None

        match = self.__key_pattern.search(tag)
        if match:
            key = match.group(1)

        match = self.__val_pattern.search(tag)
        if match:
            val = match.group(1)

        return key, val

    def exec(self, text: str = '') -> dict:
        """
        Extract Open Graph tags from text.
        :param text: Input text to extract tags.
        :return: Dict with tags found.
        """
        ret = {}
        tags = self.x_tags(text)

        for tag in tags:
            key, val = self.x_data(tag)

            if key:
                ret[key] = val

        return ret
