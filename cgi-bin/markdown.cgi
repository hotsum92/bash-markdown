#!/bin/bash -eu

echo -e "Content-Type: text/html\n"

pandoc \
  /usr/local/apache2/htdocs"$REQUEST_URI" \
  --metadata pagetitle="$REQUEST_URI" \
  -s \
  -t html5 \
  -c res/github-markdown.css
