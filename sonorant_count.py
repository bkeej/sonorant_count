import os
import csv 
import sys

sys.path.insert(1, '../uspanteko-g2p')

from uspanteko_g2p import *

# Unigraphs: [ p t k q s x j ' ]
# Bigraphs: [ b' t' k' q' tz ch ]
# Trigraphs: [ tz' ch' ]

sonorants = 'lmnwyɾ'
vowels = 'ieaouiːeːaːoːuː'
obstruents = 'ɓtʼkʼqʼt͡st͡ʃptkqsʃxʔt͡sʼt͡ʃʼ'

csvcorpus = 'usp_word_freq.csv'
corpus = 'uspanteko_words.txt'

counts = []

with open(csvcorpus) as f:
	word_list = [row.split(',')[0] for row in f]
	badcount = 0
	for w in word_list:
		try:
			w = g2p([w], delim=".")[0][1][0] #translate to IPA using g2p module
		except TypeError:
			# print(w, 'bad characters')
			badcount += 1
		else:
			w = ''.join(list(filter(lambda ch: ch not in '.', w)))
			counts.append([len(w), len(''.join(list(filter(lambda ch: ch in sonorants, w)))), len(''.join(list(filter(lambda ch: ch not in vowels, w))))])

print('number of words:', len(counts), '\n')
print('number of word with formatting problems:', badcount, '\n')

print('Average sonorants per unique word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average characters per unique word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel characters per unique word:', sum([x[2] for x in counts]) / len(counts), '\n')

print('-----------------\n')

with open(corpus) as f:
	for w in f:
		w = w.strip()
		counts.append([len(w), len(''.join([''.join(list(filter(lambda ch: ch in sonorants, x))) for x in w])), len(''.join([''.join(list(filter(lambda ch: ch not in vowels, x))) for x in w]))])

print('number of words:', len(counts), '\n')

print('Average sonorants per word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average characters per word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel characters per word:', sum([x[2] for x in counts]) / len(counts), '\n')


