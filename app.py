import collections
import codecs
import csv
import os

CSV_DIR = 'data'

keywords = []

for filename in os.listdir(CSV_DIR):
    with codecs.open(os.path.join(CSV_DIR, filename), 'rU', 'utf-16') as f:
        keyword_csv = csv.DictReader(f, delimiter="\t")
        keywords.extend([line for line in keyword_csv if line['Keyword']])
