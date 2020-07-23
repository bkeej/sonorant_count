import os
import csv 
from collections import defaultdict

corpus = 'uspanteko_words.txt'

def def_value(): 
    return False

d = defaultdict(def_value)

with open(corpus, "r") as infile:
	for w in infile:
		w.strip()
