from pathlib import Path


class Content:
    def __init__(self):
        self.title = "Hello World"
        self.subtitle = "Hey all, scott here!"
        self.body = "<b>Hello World</b>"


class Item:
    def __init__(self, href, caption):
        self.href = href
        self.caption = caption


class NavItems:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, i):
        return self.items.__getitem__(i)

    def __len__(self):
        return self.items.__len__()

    def set_paths_relative_to(self, path):
        """
        Set the links of the nav items as if they were a relative path from `path` to destination.
        """

        new_items = []
        # TODO:
        # Assume, for now, all links are paths
        for item in self.items:
            item_path = Path(item.href)
            new_path = ""
            for i in range(0, len(path.parents) - 2):
                new_path += "../"
            new_path = Path(new_path).joinpath(item_path).as_posix()
            new_items.append(Item(new_path, item.caption))
        self.items = new_items
