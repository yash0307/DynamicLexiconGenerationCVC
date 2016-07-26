### git@yash0307 ###
import gensim
import numpy as np
from nltk.corpus import stopwords
import json

stop_words = set(stopwords.words('english'))
stop_words_str = [str(i).lower() for i in stop_words]
stop_words_post_space  = [str(i) + " " for i in stop_words_str]
stop_words_pre_space = [" " + str(i) for i in stop_words_str]

jaderberg_dict = []

with open('dictnet_vgg_labels.txt') as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    for i in content:
        jaderberg_dict.append(str(i).lower())

jad_sw = []
for i in jaderberg_dict:
    try:
        given_word = str(i)
        #if ((given_word not in jad_sw) and (given_word not in stop_words_str) and (given_word not in stop_words_post_space) and (given_word not in stop_words_pre_space)):
        if (given_word not in jad_sw):
            jad_sw.append(given_word)
    except:
        pass

fp = open('jad.json','w')
json.dump(jad_sw,fp)
