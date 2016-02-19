import nltk,sys,os
from nltk import word_tokenize
from collections import defaultdict


# words = {word: [bool, num_words, num_files] }
# idf_words = {word:#docs}


def count_words(raw_text, words):
	tokens = word_tokenize(raw_text)
	for word in set(tokens):
		num = tokens.count(word)
		if num < 2:
			continue
		
		num_docs = words[word]
		num_docs +=1
		words[word] = num_docs
	return words



def calculate_idf(words,num_docs,ccsw):
	closed_class_stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among',\
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on',\
                           'onto','out','over','past','per','plus','since','till','to','under','until','up',\
                           'via','vs','with','that','can','cannot','could','may','might','must',\
                           'need','ought','shall','should','will','would','have','had','has','having','be',\
                           'is','am','are','was','were','being','been','get','gets','got','gotten',\
                           'getting','seem','seeming','seems','seemed',\
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my',\
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another',\
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not',\
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more',\
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite',\
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such',\
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which',\
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday',\
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever',\
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he',\
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs',\
                           'you','your','yours','me','my','mine','I','we','us','much','and/or','STOP'
                           ]

	idf_words = defaultdict(int)
	for word in words:
		if ccsw:
			if word in closed_class_stop_words:
				continue
		idf = float(num_docs) / float(words[word])
		idf_words[word] = idf
	return idf_words


def output_to_text_file (idf_words):
	out_string = ''
	for word in sorted(idf_words, key=idf_words.get, reverse = True):
		out_string += word + '\t' + str(idf_words[word]) + '\n'

	out_file = open('out_file.txt',"w")
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





		

			

