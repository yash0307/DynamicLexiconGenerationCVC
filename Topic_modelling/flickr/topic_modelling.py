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
data_corpus = []
print str(len(data.keys()))
for i in data.keys():
    val = data[i]
    data_corpus.append(val)


id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
corpus = [id2word.doc2bow(text) for text in data_corpus]
gensim.corpora.MmCorpus.serialize('/home/yash/Data/flickr/corpus.mm',corpus)
