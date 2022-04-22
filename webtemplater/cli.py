from .generator import Generator
from .config import Config


def main():
    config = Config("config.ini")
    generator = Generator(config)
    generator.create_site()
