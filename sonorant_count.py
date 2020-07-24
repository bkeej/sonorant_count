import os
import csv 
import sys

sys.path.insert(1, '../uspanteko-g2p')

from uspanteko_g2p import *

# Unigraphs: [ p t k q s x j ' ]
# Bigraphs: [ b' t' k' q' tz ch ]
# Trigraphs: [ tz' ch' ]

sonorants = 'lmnwyɾ'
vowels = 'íéáóúieaouiːeːaːoːuː,íːéːáːóːúː'
obstruents = 'ɓtʼkʼqʼt͡st͡ʃptkqsʃxʔt͡sʼt͡ʃʼ'

csvcorpus = 'usp_word_freq.csv'
corpus = 'uspanteko_words.txt'

counts = []

with open(corpus) as f:
	badcount = 0
	for w in f:
		w = w.strip()
		try:
			w = g2p([w], delim=".")[0][1][0] #translate to IPA using g2p module
		except TypeError:
			# print(w, 'bad characters')
			badcount += 1
		else:
			w = ''.join(list(filter(lambda ch: ch not in '.', w)))
			counts.append(
				[len(w), 
				len(''.join(list(filter(lambda ch: ch in sonorants, w)))), 
				len(''.join(list(filter(lambda ch: ch not in vowels, w)))),
				len(''.join(list(filter(lambda ch: ch in vowels, w)))),
				len(''.join(list(filter(lambda ch: ch in obstruents, w)))),
				w])

print('Computed over tokens in the combined OKMA and Bennett & Henderson corpus.\n')

print('number of words:', len(counts), '\n')

print('number of word with formatting problems:', badcount, '\n')

print('Average sonorants per word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average segments per word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel segments per word:', sum([x[2] for x in counts]) / len(counts), '\n')

print('Raw count of sonorants:', sum([x[1] for x in counts]), '\n')
print('Raw count of vowels:', sum([x[3] for x in counts]),'\n')
print('Raw count of obstruents:', sum([x[4] for x in counts]),'\n')
print('Words containings only sonorants:', len([x for x in counts if x[0] == x[1]+x[3]]), '\n')

print('\n-----------------\n')

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
			counts.append(
				[len(w), 
				len(''.join(list(filter(lambda ch: ch in sonorants, w)))), 
				len(''.join(list(filter(lambda ch: ch not in vowels, w)))),
				len(''.join(list(filter(lambda ch: ch in vowels, w)))),
				len(''.join(list(filter(lambda ch: ch in obstruents, w)))),
				w])

print('Computed over unique words (types) in the combined OKMA and Bennett & Henderson corpus.')

print('number of words:', len(counts), '\n')

print('number of word with formatting problems:', badcount, '\n')

print('Average sonorants per unique word:', sum([x[1] for x in counts]) / len(counts), '\n')

print('Average segments per unique word:', sum([x[0] for x in counts]) / len(counts), '\n')

print('Average non-vowel segments per unique word:', sum([x[2] for x in counts]) / len(counts), '\n')

print('Raw count of sonorants:', sum([x[1] for x in counts]), '\n')
print('Raw count of vowels:', sum([x[3] for x in counts]),'\n')
print('Raw count of obstruents:', sum([x[4] for x in counts]),'\n')


print('Words containings only sonorants:', len([x for x in counts if x[0] == x[1]+x[3]]),'\n')

for i in [x[5] for x in counts if x[0] == x[1]+x[3]]:
	print(i, '\n')