.ONESHELL:

.PHONY: start
start: # Deploy container, install dependencies and run server
start:
	docker-compose up
