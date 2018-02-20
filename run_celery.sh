#!/bin/sh


cd dockerize  

su -m root -c "celery worker -B -A dockerize.celeryconf -Q default -n default@%h" 

