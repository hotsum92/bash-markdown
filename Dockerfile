FROM httpd:2.4.58

run apt update && apt install -y pandoc

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
