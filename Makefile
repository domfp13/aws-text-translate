# Created By Enrique Plata

SHELL = /bin/bash

include .env

PHONY: run
run: ## (local): Runs code from container
	@ docker image build --rm -t dpeimage .
	@ docker container run --rm -it \
 	  -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} \
 	  -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} \
 	  --name runner dpeimage

help:
	@ echo "Please use \`make <target>' where <target> is one of"
	@ perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help

