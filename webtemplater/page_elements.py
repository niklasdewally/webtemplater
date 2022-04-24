from pathlib import Path


class PageContent:
    def __init__(self):
        self.title = "Hello World"
        self.subtitle = "Hey all, scott here!"
        self.body = "<b>Hello World</b>"


class NavItem:
    def __init__(self, href: str, caption: str):
        self.href = href
        self.caption = caption


class NavItemList:
    def __init__(self, items: list[NavItem]):
        self.items = items
        self.originalitems = items

    def __getitem__(self, i: int) -> NavItem:
        return self.items.__getitem__(i)

    def __len__(self) -> int:
        return self.items.__len__()

    def set_paths_relative_to(self, directory: Path):
        """
        Set the links of the nav items as if they were a relative path from the given directory.
        """
        # TODO:
        # Assume, for now, all links are paths
        for item in self.originalitems:
            new_path = os.reldir(item.href, directory)
            new_items.append(NavItem(new_path, item.caption))
        self.items = new_items
