import os
import csv 
import xml.etree.ElementTree as ET 


def igtxml_get_words(dir,xmlfile):
	with open(dir + xmlfile) as f:
		tree = ET.parse(f)
		root = tree.getroot()

		word_list = []

		for phrase in root.findall('./body/phrases/phrase'):
			word_list = word_list + phrase.findall('word')

		word_list = [x.get('text') for x in word_list]

		word_list = [''.join(list(filter(lambda ch: ch not in " :+.!¡¿?-,", x))) for x in word_list]

	return word_list

def elan_get_words(dir,eaffile):
	with open(dir + eaffile) as f:
		tree = ET.parse(f)
		root = tree.getroot()

		word_list = []

		for phrase in root.findall("./TIER[@TIER_ID='Transcripción']/ANNOTATION/ALIGNABLE_ANNOTATION/ANNOTATION_VALUE"):
			for word in phrase.text.split():
				word_list.append(word)

		word_list = [''.join(list(filter(lambda ch: ch not in " :+.!¡¿?-,", x))) for x in word_list]

		word_list = list(filter(lambda w: ">" not in w, word_list))

	return word_list


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

	print(len(words))

if __name__ == '__main__':
	main() 

