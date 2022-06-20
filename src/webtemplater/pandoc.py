from pathlib import Path
import subprocess
import json


def convert_to_html(path: Path) -> str:
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


def get_metadata_value(key: str, path: Path) -> str:
    """
    Get the value of a particular key in the pandoc metadata stored within the file

    key: the key to fetch the value for in the metadata.

    path: a Path object representing the file to extract the metadata from.

    Returns: the value of the given key in the metadata, or None.
    """

    # read the metadata from the haskell abstract syntax tree
    data = subprocess.run(
        ["pandoc", "-t", "json", "--shift-heading-level-by", "1", path.resolve()],
        capture_output=True,
        encoding="UTF-8",
    ).stdout

    ast = json.loads(data)

    # ensure that the key is in the ast:
    if ast.get("meta", None) is None:
        return None
    if ast["meta"].get(key, None) is None:
        return None
    if ast["meta"][key].get("c", None) is None:
        return None

    content = ast["meta"][key]["c"]

    # note, this is in the form of
    # "meta":{"title":{"t":"MetaInlines","c":[{"t":"Str","c":"Command"},{t:"Space"},{t:"Str",c:"Reference"}]}}

    # join together content elements (Str and Space types) into single string
    content_str = ""
    for i in range(0, len(content)):
        match content[i]["t"]:  # check haskell types
            case "Str":
                content_str += content[i]["c"]
            case "Space":
                content_str += " "

    return content_str
