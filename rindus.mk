.ONESHELL:

.PHONY: start
start: # Install dependencies and run server
start:
	pip install -r requirements.txt
	echo "Requirements installed"
	cd rindustest
	cp .pg_service.conf $(HOME)
	echo "Postgres conf file copied to user home folder"
	python manage.py migrate api && python manage.py runserver
