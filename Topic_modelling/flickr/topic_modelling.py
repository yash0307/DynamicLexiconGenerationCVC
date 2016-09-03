### git@yash0307 ###

# Read the captions + words for each image.
# Make one string for each image.
# Tokenize
# Remove stopwords and '.'

import json
from nltk import word_tokenize
from nltk.corpus import stopwords
import gensim
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

fp = open('/home/yash/Data/data.json','r')
data = json.load(fp)
data_corpus = []
for i in data.keys():
    val = data[i]
    data_corpus.append(val)

tok_corpus = []
for i in data_corpus:
    temp_tokens = [j.lower() for j in word_tokenize(i)]
    tok_corpus.append(temp_tokens)

id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')
corpus = [id2word.doc2bow(text) for text in tok_corpus]
gensim.corpora.MmCorpus.serialize('/home/yash/Data/flickr/corpus.mm',corpus)
