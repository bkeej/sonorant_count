import os
import csv 
from collections import defaultdict

import pylab
import matplotlib.pyplot as plt

corpus = 'uspanteko_words.txt'
outfile = 'usp_word_freq.csv'

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


# plotting the frequency data as a sanity check

a = list(d.values())

a.sort(reverse=True)

print(a)

fig = plt.figure()
ax = fig.add_subplot(2, 1, 1)

line, = ax.plot(a, color='blue', lw=2)

ax.set_yscale('log')
ax.set_xscale('log')

pylab.show()
