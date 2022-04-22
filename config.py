import configparser
from content import Item, Content, NavItems


class Config:
    def __init__(self, path: str):
        self.file = path
        self.config = configparser.ConfigParser()
        self.config.read(path)
        self._parse_navlinks()
        self._parse_globals()

    def _parse_navlinks(self):
        self.navitems = []
        for (label, href) in self._parse_section("navlinks").items():
            # strip quotes just in case
            self.navitems.append(Item(href.strip('"'), label))
        self.navitems = NavItems(self.navitems)

    def _parse_globals(self):
        dic = self._parse_section("site")
        self.content_root = dic["contentroot"]

    def _parse_section(self, section: str):
        return self.config[section]
