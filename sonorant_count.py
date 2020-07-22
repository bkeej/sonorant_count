import os
import csv 
import xml.etree.ElementTree as ET 

narrative_dir = '../../Recordings/2019_narratives/Completed_transcriptions/'

palmer_dir = '../special-eureka/data/uspanteko_corpus_xml/'

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

	return word_list

eaffile = "SPK_TAML_2020_Loq'laj teew pach loq'laj q'iij - El viento del norte y el sol.eaf"
xmlfile = "1.xml"

def main():

	print(elan_get_words(narrative_dir,eaffile))

	print(igtxml_get_words(palmer_dir,xmlfile))

if __name__ == '__main__':
	main() 

