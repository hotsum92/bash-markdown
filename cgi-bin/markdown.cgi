#!/bin/bash -eu

echo -e "Content-Type: text/html\n"

pandoc \
  /usr/local/apache2/htdocs"$REQUEST_URI" \
  --metadata pagetitle="$REQUEST_URI" \
  -s --self-contained \
  -t html5 \
  -c /usr/local/apache2/cgi-bin/github-markdown.css
