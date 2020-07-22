import os
import csv 
import xml.etree.ElementTree as ET 

narrative_dir = '../../Recordings/2019_narratives/Completed_transcriptions/'

palmer_dir = '../special_eureka/uspanteko_corpus_xml/'

def get_words(dir,xmlfile):
	tree = ET.parse(dir + xmlfile)
	root = tree.getroot()

	word_list = []

	for phrase in root.findall('./body/phrases/phrase'):
		word_list = word_list + phrase.findall('word')
	
	return word_list