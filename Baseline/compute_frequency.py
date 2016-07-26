### git@yash0307 ###
import gensim
import json
from nltk import word_tokenize
from nltk.corpus import stopwords
# Read Our dictionary first.
#id2word = gensim.corpora.Dictionary.load_from_text('./Dictionary/jad_sw_gensim_dict.txt')
stop_words = set(stopwords.words('english'))
stop_words_str = [str(i).lower() for i in stop_words]
# Parse the dictionary and Preprocess.
#iterator = id2word.iteritems()
#keys = id2word.keys()
#dict_list = []
#for i in range(0,len(keys)):
#    temp_item = iterator.next()
#    try:
#        dict_list.append(str(temp_item[1]).lower())
#    except:
#        pass
dict_list = []
for i in stop_words_str:
    dict_list.append(str(i))
# Read Jaderberg's dictionary.
#jaderberg_dict = []
#with open('./Dictionary/dictnet_vgg_labels.txt') as f:
#    content = f.readlines()
#    content = [x.strip('\n') for x in content]
#    for i in content:
#        jaderberg_dict.append(str(i).lower())

# Read the work-frequency file.
word_frequency = {}
with open('/media/DADES/yash/Wiki/wikipedia_wordfreq.txt') as fp:
    content = fp.readlines()
    content = [x.strip('\n') for x in content]
    for i in content:
        temp_id = str(str(i).split('\t')[0]).lower()
        temp_val = int(str(i).split('\t')[1])
        word_frequency[temp_id] = temp_val

# Assign the frequency to dict words.
our_dict_frequency = {}
for i in dict_list:
    try:
        our_dict_frequency[i] = word_frequency[i]
    except:
        our_dict_frequency[i] = 0.5

rank_our = []

for ind in our_dict_frequency.keys():
    val = our_dict_frequency[ind]
    temp = (ind,val)
    rank_our.append(temp)
rank_our = sorted(rank_our, key=lambda x:x[1],reverse=True)
fp = open("./Ranked_dict/stop_words.txt","w")
for i in rank_our:
    fp.write(i[0] + "\n")
fp.close()
#

# Assign the frequency to jabenberg dict.
#jaderberg_dict_frequency = {}
#for i in jaderberg_dict:
#    try:
#        jaderberg_dict_frequency[i] = word_frequency[i]
#    except:
#        jaderberg_dict_frequency[i] = 0.5
#
#rank_jad = []
#for ind in jaderberg_dict_frequency.keys():
#    val = jaderberg_dict_frequency[ind]
#    temp = (ind,val)
#    rank_jad.append(temp)
#rank_jad = sorted(rank_jad, key=lambda x:x[1],reverse=True)
#with open('./Ranked_dict/jad_dict.json', 'w') as fp:
#    json.dump(rank_jad, fp)
