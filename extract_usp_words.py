import os
import xml.etree.ElementTree as ET 
from timeit import default_timer as timer

sonorants = ['l', 'm', 'n', 'w', 'y', 'r']

def igtxml_get_words(dir,xmlfile):
	with open(dir + xmlfile) as f:
		tree = ET.parse(f)
		root = tree.getroot()

		word_list = []

		for phrase in root.findall('./body/phrases/phrase'):
			word_list = word_list + phrase.findall('word')

	return word_list

def elan_get_words(dir,eaffile):
	with open(dir + eaffile) as f:
		tree = ET.parse(f)
		root = tree.getroot()

		word_list = []

		for phrase in root.findall("./TIER[@TIER_ID='Transcripción']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE"):
			for word in phrase.text.split():
				word_list.append(word.lower())

	return word_list

def de_espanol(wordlist):
	with open('espanol.txt', encoding="ISO-8859-1") as f:
		esp = []
		for w in f:
			esp.append(w.rstrip())
		print('built spanish dictionary')
		wordlist =  list(filter(lambda w: w not in esp, wordlist))
	return wordlist

def main():

	narrative_dir = '../../Recordings/2019_narratives/Completed_transcriptions/'
	palmer_dir = '../special-eureka/data/uspanteko_corpus_xml/'
	igxml_files = os.listdir(palmer_dir)
	eaf_files = [f for f in os.listdir(narrative_dir) if f.endswith('.eaf')]

	words = []

	for file in igxml_files:

		words = words + igtxml_get_words(palmer_dir, file)

	for file in eaf_files:

		words = words + elan_get_words(narrative_dir, file)

	words = [x.get('text') for x in words]

	words = [x.lower() for x in words]

	words = list(filter(lambda w: "<" not in w, words))

	words = list(filter(lambda w: ">" not in w, words))

	words = [''.join(list(filter(lambda ch: ch not in " :+.!¡¿?-,<,>,(,),_,0,1,2,3,4,5,6,7,8,9,/,\\", x))) for x in words]

	words = [x.replace('ã³', 'ó')]

	words = [x.replace('ã±', 'ñ')]	

	words = [x.replace('ã', 'á')]

	words = [x.replace('pwes', pues)]

	print('Total words:', len(words))

	start = timer()
	words = de_espanol(words)
	end = timer()

	print('filtered spanish words in:', (end - start), "seconds")

	print('Non-borrowings:', len(words))

	with open('uspanteko_words.txt', 'w') as outfile:
		for w in words:
			outfile.write(w + '\n')

if __name__ == '__main__':
	main() 

