---
title: Command Reference
---
```sh
usage: python3 -m webtemplater [-h] {init,gen} ...

positional arguments:
  {init,gen}
    init      initialise a new website
    gen       generate website content

options:
  -h, --help  show this help message and exit

```
# webtemplater init

```sh
usage: python3 -m webtemplater init [-h] [-c CONTENT_DIR] [-s SITE_DIR] [-T TEMPLATE_DIR]

options:
  -h, --help            show this help message and exit
  -c CONTENT_DIR, --content-dir CONTENT_DIR
                        specify the content dir
  -s SITE_DIR, --site-dir SITE_DIR
                        specify the site dir
  -T TEMPLATE_DIR, --template-dir TEMPLATE_DIR
                        specify the template dir
```

# webtemplater gen
```sh
usage: python3 -m webtemplater gen [-h]

options:
  -h, --help  show this help message and exit
```
