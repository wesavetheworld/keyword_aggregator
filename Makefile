RESULTS=results.csv

all: build check

build:
	-mv ~/Downloads/download-*.csv data

check:
	python app.py > ${RESULTS}