.PHONY: setup auth publish_web

setup:
	virtualenv .
	./bin/pip install -r requirements.txt

auth:
	./bin/python auth.py


publish_web:
	gsutil cp ./web/*.* gs://arakawatomonori-wakari-web/
	gsutil acl set public-read gs://arakawatomonori-wakari-web/*.*
