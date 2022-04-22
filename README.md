# webtemplater

A simple static-site generator using python and pandoc.

This was created to scratch a personal itch - pandoc supports a wide range of syntax, and handles math impeccably, but making full size sites with it is cumbersome and involves some [bash](http://hamwaves.com/pandoc/article/en/makefile) [magic](https://wstyler.ucsd.edu/posts/pandoc_website.html). Also, changing things like navigation links would require manually editing each template.

webtemplater provides configuration options to easily add a custom navbar to pages, and uses a (in my opinion) simpler templating syntax.

## Features

## Usage

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
