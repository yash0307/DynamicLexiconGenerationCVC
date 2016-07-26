### git @ yash0307 ###

# Read each per-image lexicon.
# Find rank of each image transcritpion
# Save in results file.

import json

input_data_file = "/media/DADES/yash/ICDAR_per_image_lexicon/gt_train/GT_DATA.json"
input_file = open(input_data_file,"r")
GT_DATA = json.load(input_file)
f = open("results_eval.txt","w")
counter = 0
for ind in GT_DATA.keys():
    counter += 1
    print str(counter)
    input_lex_url = "/media/DADES/yash/ICDAR_per_image_lexicon/train/" + str(ind) + ".json"
    input_lex = open(input_lex_url,"r")
    final_ranks = json.load(input_lex)
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
