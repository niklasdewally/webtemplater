# webtemplater

A simple static-site generator using python and pandoc.

This was created to scratch a personal itch - pandoc supports a wide range of syntax, and handles math impeccably, but making full size sites with it is cumbersome and messy.

webtemplater provides configuration options to easily add a custom navbar to pages, and uses a (in my opinion) simpler templating syntax.

## Usage

## Writing Templates

Templates use HTML and the [Jinja](https://jinja.palletsprojects.com/) templating engine.


The following variables are supported in custom templates:

- `content.title`
- `content.subtitle`
- `content.body` - the body of the article (as HTML).

Inside of a `{% for item in nav %}` loop:
- `item.href` - the url of the nav link.
- `item.caption` - the name of the nav link.
