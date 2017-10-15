server side:
brew install gdal

+ init:
createsuperuser

+ local:
create database etc

+ PostgreSQL:
create extension postgis;

+ heroku:
git branch
env variables
- geo
- django settings
stack 14, not stack 16 (GDAL issue)

before deploy:
- git add
- makemigrations
- commit
- push
- syncdb???



http://www.marinamele.com/2014/01/how-to-set-django-app-on-heroku-part-iii.html
