# Quickstart

```bash
python build_site.py
```

# Preparation

- Install relevant packages
- Generate `pygments.css`

```bash
pygmentize -S default -f html > site/pygments.css
```

# Wiki Structure

- source (the actual site's code)
    + images
    + pages
    + style
    + templates

- output (the root of the server)
    + images
    + style