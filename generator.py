import jinja2

class Content:
    def __init__(self,title,subtitle):
        self.title = title;
        self.subtitle = subtitle;
        self.body= "<ul><li>body</li></ul>"

class Item:
    def __init__(self,href,caption):
        self.href = href;
        self.caption = caption;


# From docs
# https://stackoverflow.com/questions/38642557/how-to-load-jinja-template-directly-from-filesystem

templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
env = jinja2.Environment(loader=templateLoader);
template = env.get_template("content.html")

content = Content("Hello World","This is python")
nav = [Item("1","1"),Item("2","2")]
print(template.render(content=content,nav=nav))
