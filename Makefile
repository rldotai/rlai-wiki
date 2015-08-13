# Makefile for generating the website.
# Requires the Python environment to be previously set.


MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR :=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: website 


website:
	python build_site.py 

test:
	python build_test.py

directories:
	mkdir -p source/images
	mkdir -p source/pages
	mkdir -p source/style
	mkdir -p source/templates


pygments:
	pygmentize -S default -f html > source/style/pygments.css

# Start a simple server for viewing output files.
serve:
	python serve.py 

.PHONY: clean
clean:
	rm -rf $(MAKEFILE_DIR)/output/*.html
	rm -rf $(MAKEFILE_DIR)/style/*
	rm -rf $(MAKEFILE_DIR)/images/*