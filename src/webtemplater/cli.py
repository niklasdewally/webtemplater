from .generator import SiteGenerator
from .config import ConfigParser
import configparser
import argparse
from pathlib import Path


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
    parser_gen = subparsers.add_parser("gen", help="generate website content")

    args = parser.parse_args()

    if args.command:
        match args.command:
            case "gen":
                generate()
            case "init":
                init(args)
            case _:
                parser.parse_args(["--help"])
    else:
        parser.parse_args(["--help"])


def init(args):
    print("Initialising website")
    # copy default config.ini
    _init_config(args)
    #  make content dir
    Path(args.content_dir).mkdir(exist_ok=True)
    Path(args.site_dir).mkdir(exist_ok=True)
    # copy default templates
    Path("./templates").mkdir(exist_ok=True)


def _init_config(args):
    # make default config if no config already exists
    if Path("config.ini").is_file():
        print("config.ini found: using existing config")
    else:
        print("no config.ini found: creating")
        # https://stackoverflow.com/a/52217698
        with open("./config.ini", "w") as f:
            conf = configparser.ConfigParser(allow_no_value=True)
            conf.add_section("site")
            conf.add_section("navlinks")
            conf.set("site", "contentroot", args.content_dir)
            conf.set("site", "siteroot", args.site_dir)
            conf.set("navlinks", "; Put nav-bar links here!")
            conf.set("navlinks", "; linkname = linkdestination")
            conf.write(f)


def generate():
    config = ConfigParser("config.ini")
    generator = SiteGenerator(config)
    generator.create_site()


if __name__ == "__main__":
    main()
