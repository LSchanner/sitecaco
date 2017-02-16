FROM nginx:latest

# Set locale to utf-8 to allow characters
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY mime_types /etc/nginx/mime.types
COPY nginx.conf /etc/nginx/nginx.conf
