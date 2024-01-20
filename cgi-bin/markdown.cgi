#!/bin/bash -eu

echo -e "Content-Type: text/html\n"

#echo "$REQUEST_URI"
cat /usr/local/apache2/htdocs"$REQUEST_URI"
