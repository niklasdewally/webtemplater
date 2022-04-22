import jinja2
import configparser


class Content:
    def __init__(self, path):
        self.title = "Hello World"
        self.subtitle = "Hey all, scott here!"
        self.body = "<b>Hello World</b>"


class Item:
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption


class ConfigParser:
    def __init__(self, path: str):
        self.file = path
        self.config = configparser.ConfigParser()
        self.config.read(path)

    def parse_navlinks(self):
        output = []
        for (label, href) in self._parse_section("navlinks").items():
            output.append(Item(href, label))
        return output

    def _parse_section(self, section: str):
        return self.config[section]


# From docs
# https://stackoverflow.com/questions/38642557/how-to-load-jinja-template-directly-from-filesystem
templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=templateLoader)
template = env.get_template("content.html")

content = Content("a")
nav = ConfigParser("config.ini").parse_navlinks()
print(template.render(content=content, nav=nav))
