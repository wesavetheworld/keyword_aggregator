all: build check

build:
	mv ~/Downloads/download-*.csv data

check:
	python app.py