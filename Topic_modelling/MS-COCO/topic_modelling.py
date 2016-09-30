### git@yash0307 ###

# Read the captions + words for each image.
# Make one string for each image.
# Tokenize
# Remove stopwords and '.'

import json
from nltk import word_tokenize
import gensim
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

fp = open('/home/yash/Data/flickr/data.json','r')
data = json.load(fp)
data_train = {}
for ind in data.keys():
	if ((int(ind)%2==1)):
		data_train[ind] = data[ind]

data_corpus = []
print str(len(data.keys()))
print str(len(data_train.keys()))
for i in data_train.keys():
    val = data[i]
    data_corpus.append(val)


id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
corpus = [id2word.doc2bow(text) for text in data_corpus]
gensim.corpora.MmCorpus.serialize('/home/yash/Data/flickr/corpus_train.mm',corpus)
