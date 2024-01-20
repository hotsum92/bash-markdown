FROM httpd:2.4.58

run apt update && apt install -y pandoc

COPY conf/* conf/
COPY cgi-bin/* cgi-bin/
COPY res/* res/

