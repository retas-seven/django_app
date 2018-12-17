CREATE DATABASE django_app CHARACTER SET = UTF8;

CREATE USER django_app_user IDENTIFIED BY 'django_app_user!';

GRANT ALL ON django_app.* TO django_app_user;
