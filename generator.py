import jinja2
import configparser
import os
import subprocess
from config import Config
from pathlib import Path
from content import Content


def convert_to_html(path: Path):
    """ 
    Convert a file to html using pandoc.

    path: a Path object representing the file to be converted to html.

    Returns: a string containing the html
    """

    return subprocess.run(
        ["pandoc", "-t", "html", "--shift-heading-level-by", "1", path.resolve()],
        capture_output=True,
        encoding="UTF-8",
    ).stdout


def create_site(root, template, nav):
    ##https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python
    for file_path in Path(root).glob("**/*"):
        if file_path.is_file():

            output_path = Path("./site").joinpath(
                file_path.with_suffix(".html").relative_to(root)
            )

            # Get backwards relative path from html file to css file
            css_path = ""
            for i in range(0, len(output_path.parents) - 1):
                css_path += "../"

            css_path += "style.css"
            print("Processed " + output_path.as_posix())

            content = Content()
            content.body = convert_to_html(file_path)
            content.title = file_path.stem
            content.subtitle = ""
            nav.set_paths_relative_to(output_path)
            page = template.render(nav=nav, content=content, css_path=css_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(page)


if __name__ == "__main__":
    # From docs
    # https://stackoverflow.com/questions/38642557/how-to-load-jinja-template-directly-from-filesystem
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")
    env = jinja2.Environment(loader=templateLoader)
    template = env.get_template("content.html")
    config = Config("config.ini")

    nav = config.navitems
    content_root = config.content_root
    create_site(content_root, template, nav)
