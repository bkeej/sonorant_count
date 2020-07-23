import os
import csv 
from collections import defaultdict

corpus = 'uspanteko_words_just_B+H.txt'
outfile = 'usp_word_freq_just_B+H.csv'

def def_value(): 
    return False

d = defaultdict(def_value)

with open(corpus, "r") as infile:
	for w in infile:
		w = w.strip()
		if d[w]:
			d[w] = d[w] + 1
		else:
			d[w] = 1

with open(outfile, "w") as f:
	wri = csv.writer(f)
	wri.writerows(d.items())
