import configparser
from .page_elements import NavItem, PageContent, NavItemList


class ConfigParser:
    def __init__(self, path: str):
        self.file = path
        self.config = configparser.ConfigParser()
        # https://stackoverflow.com/a/19359720
        # Ensure config does not auto-lower case everything!
        config.optionxform = str
        self.config.read(path)
        self._parse_navlinks()
        self._parse_globals()

    def _parse_navlinks(self):
        self.navitems = []
        for (label, href) in self._parse_section("navlinks").items():
            # strip quotes just in case
            self.navitems.append(NavItem(href.strip('"'), label))
        self.navitems = NavItemList(self.navitems)

    def _parse_globals(self):
        dic = self._parse_section("site")
        self.content_root = dic["contentroot"]
        self.site_root = dic["siteroot"]
        self.template_root = dic["templateroot"]

    def _parse_section(self, section: str):
        return self.config[section]
