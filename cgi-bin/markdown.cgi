#!/bin/bash

file=/usr/local/apache2/htdocs"$REQUEST_URI"
last_modified=$(date -r "$file" -u +%a,\ %d\ %b\ %Y\ %H:%M:%S\ GMT)

if [ "$last_modified" = "$HTTP_IF_MODIFIED_SINCE" ]; then
  echo -e "Status: 304 Not Modified\n"
else
  echo -e "Status: 200 OK"
  echo -e "Last-Modified: $last_modified"
  echo -e "Content-Type: text/html\n"

  pandoc \
    /usr/local/apache2/htdocs"$REQUEST_URI" \
    --metadata pagetitle="$REQUEST_URI" \
    -s \
    -t html5 \
    --css res/github-markdown.css \
    | sed '/<\/head>/i <script src="res/refresh.js"></script>'
fi
