#!/bin/bash -eu

docker run -it --rm \
  -p 8080:80 \
  -v ./htdocs:/usr/local/apache2/htdocs \
 markdown:1.0.0
