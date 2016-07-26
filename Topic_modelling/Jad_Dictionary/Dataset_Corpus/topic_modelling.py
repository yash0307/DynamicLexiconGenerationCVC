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

fp = open('/home/yash/git_CVC/Dataset_corpus/dataset_corpus.json','r')
data = json.load(fp)
data_corpus = []
for i in data.keys():
    val = data[i]
    captions = val['caption']
    words_str = ''
    words = val['words']
    for word in words:
        words_str = words_str + ' ' + word
    temp_doc = captions + ' ' + words_str
    data_corpus.append(temp_doc)

stop_words = set(stopwords.words('english')).union('.')
stop_words_str = [str(i).lower() for i in stop_words]

# tok_corpus = []
# counter = 0
# for i in data_corpus:
#     temp_tokens = [j.lower() for j in word_tokenize(i) if j not in stop_words_str]
#     print str(temp_tokens)
#     tok_corpus.append(temp_tokens)

check_dict = []
counter = 0
for doc in data_corpus:
    counter = counter + 1
    print str(counter)
    str_doc_lst = [str(i) for i in doc.split()]
    for j in str_doc_lst:
        if((j not in check_dict) and (j not in stop_words_str)):
            check_dict.append(j)

print str(len(check_dict))
fp = open('check_dict.json','w')
json.dump(check_dict,fp)
#id2word = gensim.corpora.Dictionary.load_from_text('/media/DADES/yash/Wikipedia/jad_gensim_dict.txt')
#corpus = [id2word.doc2bow(text) for text in tok_corpus]
#gensim.corpora.MmCorpus.serialize('/media/DADES/yash/topicModelDataset/Dataset_Corpus/Jad_dict/corpus_train.mm',corpus)
