from .generator import SiteGenerator
from .config import ConfigParser


def main():
    config = ConfigParser("config.ini")
    generator = SiteGenerator(config)
    generator.create_site()


if __name__ == "__main__":
    main()
