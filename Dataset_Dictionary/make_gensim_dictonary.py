### git@yash0307 ###
import gensim
import json

fp = open('/home/yash/git_CVC/Compare_Dictionary/jad_sw.json','r')
list_of_words = json.load(fp)
dictionary_str = ''
for i in list_of_words:
    dictionary_str = dictionary_str + ' ' + str(i).lower()

gensim_dict = gensim.corpora.dictionary.Dictionary([dictionary_str.split()])
gensim_dict.save_as_text('/home/yash/git_CVC/Compare_Dictionary/jad_sw.txt')