import nltk,sys,os
from nltk import word_tokenize
from collections import defaultdict
import math


# words = {word: [bool, num_words, num_files] }
# idf_words = {word:#docs}


def count_words(raw_text, words):
	t = word_tokenize(raw_text)
	tokens = []
	for w in t:
		if len(w) < 3:
			continue
		if w.isalpha():
			tokens.append(w.lower())

	for word in set(tokens):
		num = tokens.count(word)
		if num < 2:
			continue
		num_docs = words[word]
		num_docs +=1
		words[word] = num_docs
	return words



def calculate_idf(words,num_docs,ccsw):
	
    #stop words from the internet, more comprehensive list than given
	stop_raw = open('stop_words.txt').read()
	closed_class_stop_words = stop_raw.split()

	idf_words = defaultdict(int)
	for word in words:
		if ccsw:
			if word in closed_class_stop_words:
				continue
		idf = math.log(float(num_docs) / float(words[word]))
		idf_words[word] = idf
	return idf_words


def output_to_text_file (idf_words):
	out_string = ''
	for word in sorted(idf_words, key=idf_words.get, reverse = True):
		out_string += word + ' ' + str(idf_words[word]) + '\n'

	out_file = open('idf_training.txt',"w")
	out_file.write(out_string)
	out_file.close()


def it_thru_corpus_folder(ccsw):
	folder = 'all-OANC-dir/'
	num_docs = 0
	words = defaultdict(int)
	for filename in os.listdir(folder):
		with open(os.path.join(folder,filename),"r") as current_file:
			if filename[-3:] == 'txt':
				raw = current_file.read()
				words = count_words(raw,words)
				num_docs += 1
				print (str(num_docs) + ' / 8824 Files Processed')
				# Short version, half the files
				#if num_docs > 4000:
				#	break

	idf_words = calculate_idf(words,num_docs,ccsw)
	output_to_text_file(idf_words)

b = sys.argv[1]
if int(b) == 0:
	ccsw = True
else:
	ccsw = False
it_thru_corpus_folder(ccsw)





		

			

