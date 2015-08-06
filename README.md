# Quickstart

```bash
source activate py-web
make directories
make
```

# TODO

- Better MathJax configuration
- Get the Math renderer and Highlight renderer working properly, in separate files
- Add wiki-link preprocessor
- Add actual style sheets
- Create index page
- Solve portability issue w/r/t custom environment.
    + Create own conda installer for required packages?

# Slowstart

## Preparation

- Install relevant packages
    + Ideally, using `conda` with environment `py-web`

```bash
conda create -n py-web python=3.4 anaconda
```

- Generate `pygments.css`

```bash
pygmentize -S default -f html > source/pygments.css
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
