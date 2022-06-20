# webtemplater

A simple static-site generator using python and pandoc.

This was created to scratch a personal itch - pandoc supports a wide range of syntax, and handles math impeccably, but making full size sites with it is cumbersome and involves some [bash](http://hamwaves.com/pandoc/article/en/makefile) [magic](https://wstyler.ucsd.edu/posts/pandoc_website.html). 
Also, changing things like navigation links would require manually editing the pandoc template for each site (the `<base>` tag could do this, but the base would have to be itself defined as an absolute path, which is not portable).

webtemplater provides easy configuration options to add a custom navbar to pages, and uses a (in my opinion) simpler templating syntax.

## Example

For a working example, see [/example/README.md].
## Instlalation From Source

```sh
# Clone the git repo
git clone github.com/niklasdewally/webtemplater
cd webtemplater
# Install the cloned project as a python module