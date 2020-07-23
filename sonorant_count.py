import os
import csv 

# Unigraphs: [ p t k q s x j ' ]
# Bigraphs: [ b' t' k' q' tz ch ]
# Trigraphs: [ tz' ch' ]

sonorants = 'lmnwyr'
vowels = 'ieaou'

csvcorpus = 'usp_word_freq.csv'
corpus = 'uspanteko_words.txt'

counts = []

with open(csvcorpus) as f:
	word_list = [row.split()[0] for row in f]
	for w in word_list:
		w = w.strip()
		counts.append([len(w), len(''.join([''.join(list(filter(lambda ch: ch in sonorants, x))) for x in w])), len(''.join([''.join(list(filter(lambda ch: ch not in vowels, x))) for x in w]))])

print('\nAverage sonorants per unique word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average characters per unique word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel characters per unique word:', sum([x[2] for x in counts]) / len(counts), '\n')

print('-----------------\n')

with open(corpus) as f:
	for w in f:
		w = w.strip()
		counts.append([len(w), len(''.join([''.join(list(filter(lambda ch: ch in sonorants, x))) for x in w])), len(''.join([''.join(list(filter(lambda ch: ch not in vowels, x))) for x in w]))])

print('Average sonorants per word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average characters per word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel characters per word:', sum([x[2] for x in counts]) / len(counts), '\n')

