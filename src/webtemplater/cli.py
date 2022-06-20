import importlib
from .generator import SiteGenerator
from .config import ConfigParser
import configparser
import argparse
from pathlib import Path
import shutil
import importlib.resources as res


def main():
    parser = argparse.ArgumentParser()
    # https://majornetwork.net/2020/05/subcommands-with-argument-parsing-in-python/
    subparsers = parser.add_subparsers(dest="command")
    parser_init = subparsers.add_parser("init", help="initialise a new website")
    parser_init.add_argument(
        "-c", "--content-dir", help="specify the content dir", default="./content"
    )
    parser_init.add_argument(
        "-s", "--site-dir", help="specify the site dir", default="./site"
    )
    parser_init.add_argument(
        "-T", "--template-dir", help="specify the template dir", default="./templates"
    )
    parser_gen = subparsers.add_parser("gen", help="generate website content")

    args = parser.parse_args()

    if args.command:
        match args.command:
            case "gen":
                conf = ConfigParser("./config.ini")
                init(
                    conf
                )  # ensure all necessary files are still present before proceeding!
                generate(conf)
            case "init":
                print("Initialising website")
                make_config(args)  # ensure we have a config file to init from before
                conf = ConfigParser("./config.ini")
                init(conf)
            case _:
                parser.parse_args(["--help"])
    else:
        parser.parse_args(["--help"])


def make_config(args):
    # make default config if no config already exists
    if Path("config.ini").is_file():
        print("config.ini found: using existing config")
    else:
        print("no config.ini found: creating")
        # https://stackoverflow.com/a/52217698
        with open("./config.ini", "w") as f:
            conf = configparser.ConfigParser(allow_no_value=True)
            # https://stackoverflow.com/a/19359720
            # Ensure config does not auto-lower case everything!
            conf.optionxform = str
            conf.add_section("site")
            conf.add_section("navlinks")
            conf.set("site", "contentroot", args.content_dir)
            conf.set("site", "siteroot", args.site_dir)
            conf.set("site", "templateroot", args.template_dir)
            conf.set("navlinks", "; Put nav-bar links here!")
            conf.set(
                "navlinks",
                "; these can either be urls, or links relative to the site root",
            )
            conf.set(
                "navlinks",
                "; note that all links to generated pages need to end in .html not md!",
            )
            conf.set("navlinks", "; example:")
            conf.set("navlinks", "; Home Page = home.html")
            conf.set("navlinks", "; Docs = docs/index.html")
            conf.set("navlinks", "; Google = www.google.com")
            conf.write(f)


def init(conf):

    Path(conf.content_root).mkdir(exist_ok=True)
    Path(conf.site_root).mkdir(exist_ok=True)

    _init_templates(conf)


def _init_templates(conf: ConfigParser):
    # create template dir and copy default templates
    Path(conf.template_root).mkdir(exist_ok=True)

    template_content = res.path("webtemplater", "template_content.html")
    template_header = res.path("webtemplater", "template_header.html")
    template_style = res.path("webtemplater", "template_style.css")

    # only copy each if they do not alrady exist in the template folder
    if not Path(conf.template_root, "content.html").exists():
        print("No content.html templatefound - copying default")
        shutil.copy(template_content, Path(conf.template_root, "content.html"))

    if not Path(conf.template_root, "header.html").exists():
        print("No header.html templatefound - copying default")
        shutil.copy(template_header, Path(conf.template_root, "header.html"))

    if not Path(conf.template_root, "style.css").exists():
        print("No style.css template found - copying default")
        shutil.copy(template_style, Path(conf.template_root, "style.css"))


def generate(conf):
    generator = SiteGenerator(conf)
    generator.create_site()


if __name__ == "__main__":
    main()
