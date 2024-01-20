FROM httpd:2.4.58

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

RUN sed -i '1c#!/usr/bin/perl' /usr/local/apache2/cgi-bin/printenv
RUN chmod +x /usr/local/apache2/cgi-bin/printenv
