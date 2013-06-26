all: build pep8 check

build:
	-mv ~/Downloads/download-*.csv data

pep8:
	autopep8 --in-place app.py

check:
	python app.py