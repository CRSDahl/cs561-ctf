FROM php:apache
COPY web /var/www/html/
COPY secret /
RUN chmod 777 /secret
RUN sed -i "s/Listen 80/Listen 3/" /etc/apache2/ports.conf 