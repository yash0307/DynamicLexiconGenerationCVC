### git@yash0307 ###

# Topic modelling using "LSA" and "LDA" methods
# for jaderberg's dictionary.

import gensim
# Load Jaderberg's dictionary.
jaderberg_list = ''
with open('../../Compare_Dictionary/dictnet_vgg_labels.txt') as f:
    content = f.readlines()
    content = [x.strip('\n') for x in content]
    for i in content:
        jaderberg_list = jaderberg_list + ' ' + str(i).lower()

# Make Gensim's dictionary instance.
gensim_dict = gensim.corpora.dictionary.Dictionary([jaderberg_list.split()])
gensim_dict.save_as_text('jad_gensim_dict.txt')
