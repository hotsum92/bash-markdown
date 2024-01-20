FROM httpd:2.4.58

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

run apt update && apt install -y pandoc
