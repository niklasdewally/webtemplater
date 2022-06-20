from dbus import MissingReplyHandlerException
import jinja2
import configparser
import os
import subprocess
import json
from .config import ConfigParser
from pathlib import Path
from .page_elements import PageContent
from .pandoc import convert_to_html, get_metadata_value

from shutil import copy2 as copy


def get_title(path: Path) -> str:
    metadata = get_metadata_value("title", path)
    if metadata is None:
        return path.stem
    return metadata


class SiteGenerator:
    def __init__(self, config: ConfigParser):
        templateLoader = jinja2.FileSystemLoader(searchpath=config.template_root)
        env = jinja2.Environment(loader=templateLoader)
        self.template = env.get_template("content.html")
        self.nav = config.navitems
        self.content_root = config.content_root
        self.site_root = config.site_root

    def create_site(self):
        # https://stackoverflow.com/questions/19587118/iterating-through-directories-with-python
        self._setup_site_dir()
        for file_path in Path(self.content_root).glob("**/*"):
            if file_path.is_file():
                if file_path.suffix == ".md":
                    output_path = Path(self.site_root).joinpath(
                        file_path.with_suffix(".html").relative_to(self.content_root)
                    )

                    # Get backwards relative path from html file to css file
                    css_path = os.path.relpath(
                        self.site_root + "/style.css", output_path.parent
                    )
                    print("Processed " + output_path.as_posix())

                    # Generate content
                    content = PageContent()
                    content.body = convert_to_html(file_path)
                    content.title = get_title(file_path)
                    # content.subtitle = get_subtitle(file_path)

                    # Update nav links
                    self.nav.set_paths_relative_to(
                        output_path.parent.relative_to(self.site_root)
                    )

                    page = self.template.render(
                        nav=self.nav, content=content, css_path=css_path
                    )

                    # Create output dir(s) and save html file
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_text(page)

                else:
                    output_path = Path(self.site_root).joinpath(
                        file_path.relative_to(self.content_root)
                    )
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    copy(file_path, output_path)

    def _setup_site_dir(self):
        Path("./site").mkdir(exist_ok=True)
        if not os.path.exists("./templates/style.css"):
            raise FileNotFoundError("templates/style.css not found!")
        copy("templates/style.css", self.site_root + "/style.css", follow_symlinks=True)
