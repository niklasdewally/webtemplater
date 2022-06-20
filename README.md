# webtemplater

A simple static-site generator using python and pandoc.

This was created to scratch a personal itch - pandoc supports a wide range of syntax, and handles math impeccably, but making full size sites with it is cumbersome and involves some [bash](http://hamwaves.com/pandoc/article/en/makefile) [magic](https://wstyler.ucsd.edu/posts/pandoc_website.html). 
Also, changing things like navigation links would require manually editing the pandoc template for each site.

webtemplater provides easy configuration options to add a custom navbar to pages, and uses a (in my opinion) simpler templating syntax.

## Features

## Installation

### From Source

```sh
# Clone the git repo
git clone github.com/niklasdewally/webtemplater
cd webtemplater
# Install the cloned project as a python module
pip install -e .
```

## Usage
### Initialising a site.
### Generating a site.
### Configuration

## Writing Templates

Templates use HTML and the [Jinja](https://jinja.palletsprojects.com/) templating engine.


The following variables are supported in custom templates:
- `css_path` - the relative path of the css file from the html file. The relative pathing is automatically filled in depending on the location of the site in the page.
- `content.title`
- `content.subtitle`
- `content.body` - the body of the article (as HTML).

Inside of a `{% for item in nav %}` loop:
- `item.href` - the url of the nav link.
- `item.caption` - the name of the nav link.
