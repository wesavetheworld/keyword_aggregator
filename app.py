from collections import Counter
import codecs
import csv
import os

CSV_DIR = 'data'

keywords = []
keyword_counter = Counter()

for filename in os.listdir(CSV_DIR):
    with codecs.open(os.path.join(CSV_DIR, filename), 'rU', 'utf-16') as f:
        keyword_csv = csv.DictReader(f, delimiter="\t")
        keywords.extend([line for line in keyword_csv if line['Keyword']])

for keyword in keywords:
    if keyword['Avg. monthly searches']:
        tokens = keyword['Keyword'].split(' ')
        for token in tokens:
            keyword_counter.update({
                token: int(keyword['Avg. monthly searches'])
            })

print "Keyword\tAvg. monthly searches"
for keyword in keyword_counter.most_common(1000):
    print "{0}\t{1}".format(*keyword)
