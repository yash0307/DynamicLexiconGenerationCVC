### git @ yash0307 ###

# Read each per-image lexicon.
# Find rank of each image transcritpion
# Save in results file.

import json

input_data_file = "/media/DADES/yash/ICDAR_per_image_lexicon/gt_train/GT_DATA.json"
input_file = open(input_data_file,"r")
GT_DATA = json.load(input_file)
fre_dict_file = open("/home/yash/git_CVC/Baseline/Ranked_dict/jad_sw_gensim_dict.json","r")
fre_dict = json.load(fre_dict_file)
final_ranks = []
for i in fre_dict:
    final_ranks.append(i[0])
f = open("results_eval.txt","w")
counter = 0
for ind in GT_DATA.keys():
    counter += 1
    print str(counter)
    words_present = GT_DATA[ind]
    text_ranks = []
    for text in words_present:
        try:
            text_ranks.append(str(text) + " : " + str(final_ranks.index(str(text.lower()))))
        except ValueError:
            try:
                text_ranks.append(str(text) + " : NA")
            except:
                text_ranks.append("Unicode error")
    f.write(str(text_ranks) + "\n")
    f.write("Total words : " + str(len(final_ranks)) + "\n")
    f.write("---------------------------------------\n")
    print (str(text_ranks))
    print ("Total words : " + str(len(final_ranks)))
    print ("---------------------------------------")
