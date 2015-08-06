#!/bin/bash
# A script that uses inotify-tools to recursively watch all 
# subdirectories of the current directory, and then execute
# `make website` upon any watched markdown files being modified.

trigger=*.md

while true; do
	change=$(inotifywait -rq -e close_write,moved_to,create .)
	change=${change##*/ * }
	if [[ "$change" == $trigger ]]; then make website; fi
done