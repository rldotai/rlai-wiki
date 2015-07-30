"""
Script for converting markdown to HTML.
"""
import fnmatch
import os
import shutil
from jinja2 import Environment, FileSystemLoader

from render_markdown import render_markdown


mathjax_url = "http://cdn.mathjax.org/mathjax/latest/MathJax.js"


def gen_find(pattern, top):
    for root, dirs, files in os.walk(top):
        for filename in fnmatch.filter(files, pattern):
            yield os.path.join(root, filename)


def more_recent(a, b):
    """Return `True` if `a` was more recently modified than `b`."""
    return (os.stat(a).st_mtime - os.stat(b).st_mtime) > 1


def copytree(src, dst, symlinks=False, ignore=None):
    """
    Reimplentation of copytree to handle similarly named files with different
    modification times.
    """
    if not os.path.exists(dst):
        os.makedirs(dst)
    for name in os.listdir(src):
        s = os.path.join(src, name)
        d = os.path.join(dst, name)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or more_recent(s, d):
                shutil.copy(s, d)


def main(source_dir, output_dir):
    # Directories to copy, of the form [(<source_path>, <output_path>), ...]
    to_copy = [('style', 'style'), ('images', 'images')] 

    # Directories used to build the page
    template_dir = os.path.join(source_dir, 'templates')
    page_dir = os.path.join(source_dir, 'pages')

    # Copy assets to output
    for src, dst in to_copy:
        src = os.path.join(source_dir, src)
        dst = os.path.join(output_dir, dst)
        copytree(src, dst)

    # Render pages
    env = Environment(loader=FileSystemLoader(template_dir), trim_blocks=True)
    template = env.get_template('page_template.html')
    for src in gen_find('*.md', page_dir):
        # Get the file's base name
        filename = os.path.basename(src)
        base, _ = os.path.splitext(filename)
        dst = os.path.join(output_dir, base + '.html')
        # print(src)
        # print(base)
        # print(dst)

        # Render the page body with customized markdown
        body = render_markdown(open(src, 'r').read())
        rendered = template.render(body=body, mathjax_url=mathjax_url)

        # Progress update
        print(src, '-->', dst)
        with open(dst, 'w') as f:
            f.write(rendered)






if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = os.path.join(root_dir, 'source')
    output_dir = os.path.join(root_dir, 'output')
    main(source_dir, output_dir)