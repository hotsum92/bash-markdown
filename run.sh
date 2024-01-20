#!/bin/bash -eu

docker run -it --rm \
  -p 8080:80 \
  -v ./htdocs:/usr/local/apache2/htdocs \
  -v ./cgi-bin:/usr/local/apache2/cgi-bin \
  -v ./res:/usr/local/apache2/res \
 markdown:1.0.0
