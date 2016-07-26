### git@yash0307 ###
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

id2word = corpora.Dictionary.load_from_text('/home/yash/git_CVC/Dataset_Dictionary/all_gensim_dict.txt')
wiki_corpus = corpora.wikicorpus.WikiCorpus('/media/DADES/yash/Wikipedia/enwiki-latest-pages-articles.xml.bz2.zip', dictionary=id2word)
corpora.MmCorpus.serialize("/media/DADES/yash/topicModelDataset/wiki_corpus.mm", wiki_corpus)
