import json
import gensim

f_result = open("/home/yash/Data/flickr/Results/result_30.json")
load_res = json.load(f_result)

f_gt = open("/home/yash/Data/flickr/data.json")
load_gt = json.load(f_gt)

id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/DynamicLexiconGenerationCVC/Dataset_Dictionary/gensim_flickr.txt')

# Parse the dictionary and Pre-process.
iterator = id2word.iteritems()
keys = id2word.keys()
dict_natural = {}
for i in range(0,len(keys)):
    temp_item = iterator.next()
    try:
    	dict_natural[str(temp_item[1]).lower()] = []
    except:
        pass
print str(dict_natural)
print str(len(dict_natural.keys())
