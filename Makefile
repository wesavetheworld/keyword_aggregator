RESULTS=results.csv
DOWNLOADS=~/Downloads
CSV_DIR=data

all: build check

build:
	-mv ${DOWNLOADS}/download-*.csv ${CSV_DIR}

check:
	python app.py ${CSV_DIR} > ${RESULTS}