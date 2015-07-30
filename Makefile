# Makefile for generating the website.
# Requires the Python environment to be previously set.


all: website 


website:
	python build_site.py 


pygments:
	pygmentize -S default -f html > source/style/pygments.css

# Start a simple server for viewing output files.
serve:
	python serve.py 