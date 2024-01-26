#!/bin/bash -eu

port=8080

while getopts p: OPT
do
    case $OPT in
        p) port=$OPTARG
           ;;
        \?) echo error
           ;;
    esac
done

echo "> markdown server http://localhost:$port"

docker run -it --rm -p "$port":80 -v "$PWD":/usr/local/apache2/htdocs markdown:1.0.0
