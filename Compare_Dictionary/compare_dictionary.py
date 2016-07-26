#### git@yash0307 ####
import gensim

# Read the dictionary.
id2word = gensim.corpora.Dictionary.load_from_text('/home/yash/git_CVC/Dataset_Dictionary/all_gensim_dict.txt')

# Parse the dictionary and Preprocess.
iterator = id2word.iteritems()
keys = id2word.keys()
dict_list = []
for i in range(0,len(keys)):
    temp_item = iterator.next()
    try:
        dict_list.append(str(temp_item[1]).lower())
    except:
        pass

# Now read JADERBERG's dictionary.
jaderberg_dict = []
with open('dictnet_vgg_labels.txt') as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    for i in content:
        jaderberg_dict.append(str(i).lower())

# Compare two list of dictionaries made.
print "Length of Jaderberg's dictionary : " + str(len(jaderberg_dict))
print "Length of Dataset's  dictionary : " + str(len(dict_list))

common = set(dict_list) & set(jaderberg_dict)
print "Common words : " + str(len(common))
